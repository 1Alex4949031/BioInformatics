# Домашнее задание 5. Предсказание и парное выравнивание структур белков


## 1. Общая информация

Мой инструмент 1 фолдинга белков: [**RoseTTAFold2**](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/RoseTTAFold2.ipynb)  

Мой инструмент 2 фолдинга белков: [**AlphaFold2**](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)

Моя последовательность: _MDADVISFEASRGDLVVLDAIHDARFETEAGPGVYDIHSPRIPSEKEIEDRIYEILDKIDVKKVWINPDCGLKTRGNDETWPSLEHLVAAAKAVRARLDK_  

Мой инструмент парного выравнения: [**CLICK**](https://mspc.bii.a-star.edu.sg/minhn/pairwise.html) - **НЕ РАБОТАЕТ**

Выбрал другой инструмент -  [**jCE (в списке Alignment Method)**](https://www.rcsb.org/alignment)

## 2. Работа в Google Collab

Файлы ipynb расположены в папке colab.

Самое главное на этом шаге поставить правильную среду выполнения:

1) Среда выполнения
3) Сменить среду выполнения
4) Ставить вариант с GPU, иначе придётся ждать миллион лет

## 3. Предсказания

Все результаты для каждого из этих инструментов находят в соответствующих папках.

То есть для AlphaFold2 идёт папка alphaFold2, а для RoseTTAFold2 идёт roseTTAFold2.

Также добавил папку collab с копиями блокнотов AlphaFold2 и RoseTTAFold2.

## 4. Инструмент парного выравнивания

Загрузил оба результата в формате pbe (лежат в папку /pairwise)

Воспользовался [**jCE (в списке Alignment Method)**](https://www.rcsb.org/alignment) инструментом парного выравнивания.

![image](https://github.com/user-attachments/assets/e9ea3892-5692-4c2b-9c7f-08073f8d590e)

## 5 и 6. Визуализация и видео

Фотография:

![model](https://github.com/user-attachments/assets/543c4c9b-1503-4dac-a989-3354467be1ad)

Видео:

https://github.com/user-attachments/assets/a1c84b36-428b-48fe-95dc-9f6ce30ab51e

## 7. Выводы

Выводы по результатам выравнивания структур

**1) RMSD (Root Mean Square Deviation):**

- Для модели AlphaFold2 значение RMSD составляет 0.61.

- Это указывает на небольшие отличия между моделями.

**2) TM-score (Template Modeling Score):**

- Для AlphaFold2 значение TM-score равно 0.98.

- Это высокий показатель, свидетельствующий о том, что структуры схожи друг с другом.

**3) Identity (Идентичность последовательностей):**

- Для RoseTTAFold2 и AlphaFold2 значения идентичности между структурами составляют 100%.

- Это означает, что все аминокислотные остатки в выравнивании идеально совпадают между моделями. 

**4) Aligned Residues (Выравненные остатки):**

- Для AlphaFold2 выровнены 100 остатков. Это также подтверждает, что обе структуры полностью совпадают по аминокислотной последовательности и не имеют пропусков.

**5) Sequence Length (Длина последовательности):**

- Для обеих структур длина последовательности составляет 100 остатков, что означает, что обе структуры относятся к одному и тому же белковому фрагменту или полному белку.

**6) Modeled Residues (Моделированные остатки):**

- Для AlphaFold2 указано, что все 100 остатков были смоделированы, что также подтверждает полное покрытие белка.

  
