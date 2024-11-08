from prefect import flow, task
import subprocess

# Пороговое значение качества
THRESHOLD = 90.0

@task
def run_flagstat(input_bam):
    # Запускаем команду samtools flagstat
    result = subprocess.run(["wsl", "samtools", "flagstat", input_bam], capture_output=True, text=True)
    return result.stdout

@task
def parse_flagstat_output(flagstat_output):
    # Извлекаем процент выравненных ридов
    for line in flagstat_output.splitlines():
        if "mapped (" in line:
            mapped_percentage = float(line.split("(")[1].split("%")[0])
            return mapped_percentage
    return 0.0

@task
def evaluate_alignment(mapped_percentage):
    # Сравниваем с порогом
    if mapped_percentage >= THRESHOLD:
        print("OK")
    else:
        print("not OK")

@flow
def quality_assessment_pipeline(input_bam):
    # Шаги пайплайна
    flagstat_output = run_flagstat(input_bam)
    mapped_percentage = parse_flagstat_output(flagstat_output)
    evaluate_alignment(mapped_percentage)

# Запускаем пайплайн
quality_assessment_pipeline("aln-se.sorted.bam")
