import logging
from prefect import flow, task, get_run_logger
import subprocess

# Пороговое значение качества
THRESHOLD = 90.0

# Настраиваем логгирование в файл
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler() 
    ]
)
logger = logging.getLogger(__name__)

@task
def run_flagstat(input_bam):
    logger = get_run_logger()
    logger.info(f"Запускаем samtools flagstat для файла: {input_bam}")
    
    # Запускаем команду samtools flagstat через WSL
    result = subprocess.run(["wsl", "samtools", "flagstat", input_bam], capture_output=True, text=True)
    
    # Логируем результат команды
    if result.returncode == 0:
        logger.info("Команда samtools flagstat выполнена успешно")
    else:
        logger.error("Ошибка выполнения samtools flagstat")
    
    return result.stdout

@task
def parse_flagstat_output(flagstat_output):
    logger = get_run_logger()
    logger.info("Парсинг результата samtools flagstat для извлечения процента выравнивания")

    # Извлекаем процент выравненных ридов
    mapped_percentage = 0.0
    for line in flagstat_output.splitlines():
        if "mapped (" in line:
            mapped_percentage = float(line.split("(")[1].split("%")[0])
            logger.info(f"Найден процент выравненных ридов: {mapped_percentage}%")
            break
    
    # Логируем, если процент не найден
    if mapped_percentage == 0.0:
        logger.warning("Процент выравненных ридов не найден, возвращено значение 0.0")
    
    return mapped_percentage

@task
def evaluate_alignment(mapped_percentage):
    logger = get_run_logger()
    logger.info(f"Оценка качества картирования: {mapped_percentage}%")
    
    # Определяем результат
    result = "OK" if mapped_percentage >= THRESHOLD else "not OK"
    logger.info(f"Результат: {result}")
    print(result)
    
    return result

@task
def save_results(mapped_percentage, evaluation_result):
    # Записываем результаты в файл
    with open("mapping_results.txt", "w") as result_file:
        result_file.write("Результаты картирования:\n")
        result_file.write(f"Процент выравненных ридов: {mapped_percentage}%\n")
        result_file.write(f"Оценка: {evaluation_result}\n")
    print("Результаты сохранены в файл mapping_results.txt")

@flow
def quality_assessment_pipeline(input_bam):
    logger = get_run_logger()
    logger.info("Запуск пайплайна оценки качества картирования")
    
    # Шаги пайплайна
    flagstat_output = run_flagstat(input_bam)
    mapped_percentage = parse_flagstat_output(flagstat_output)
    evaluation_result = evaluate_alignment(mapped_percentage)
    
    # Сохранение итоговых результатов в файл
    save_results(mapped_percentage, evaluation_result)

# Запускаем пайплайн
quality_assessment_pipeline("aln-se.sorted.bam")
