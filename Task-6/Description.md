# Домашнее задание 6. Докинг лекарственных молекул


## 1. Общая информация о препарате

**Коммерческое наименование:** Каптоприл

a. **Действующее вещество**: Каптоприл (Captopril).
  
b. **Область применения:** Каптоприл применяется для лечения:

- Артериальной гипертензии (повышенного артериального давления).

- Сердечной недостаточности.

- Диабетической нефропатии (особенно при сахарном диабете 1 типа).

- Состояния после инфаркта миокарда для улучшения функций сердца.

c. **Молекулярный механизм действия:** Каптоприл является ингибитором ангиотензин-превращающего фермента (АПФ).

Он блокирует фермент, преобразующий ангиотензин I в ангиотензин II — вещество, которое вызывает сужение кровеносных сосудов и повышает артериальное давление. Путем ингибирования образования ангиотензина II, каптоприл:

1. Снижает тонус сосудов.
2. Уменьшает общее периферическое сосудистое сопротивление.
3. Уменьшает задержку натрия и воды в организме, что также снижает давление.

Эти эффекты помогают снизить артериальное давление и уменьшить нагрузку на сердце.

**Немного терминалогии:**

- Ангиотензинпревращающий фермент (ACE) — это фермент, который играет ключевую роль в регуляции кровяного давления и баланса жидкости в организме.
Он принадлежит к группе металлопротеиназ и встречается на поверхности клеток, в основном в легких, почках и сосудах.

## 2. Работа с google colab

1. PDB ID представляет структуру мишени — Angiotensin-Converting Enzyme (ACE).

Во всех блоках кода, где требуется указать мишень, используем 1O86.

2. В 4 пункте вставляем SMILES

SMILES для каптоприла: C[C@H](CS)C(=O)N1CCC[C@H]1C(O)=O

3. Укажем keyword: LPR

Keyword — это идентификатор для маркировки выходных данных, чтобы связать их с вашим экспериментом.

4. Сохранение результатов

Все результаты сохранены в папку Captopril_1O86.

Использованный блокнот с доработками - Task6.ipynv

## 3. Полученные результаты докинга
Все результаты сохранены в папку Captopril_1O86/DOCKING/SIM.

## 4. Изображения

1. Трёхмерная структура

![image](https://github.com/user-attachments/assets/bf7a0e89-b799-43c9-bec2-ba4de585c330)

2. Трехмерная структура исходного лиганда

![image](https://github.com/user-attachments/assets/7ad8fdaf-bba3-4976-82d1-6aa1c30b7dd8)

3. Полученный бокс

![image](https://github.com/user-attachments/assets/294a1e31-e186-4c17-a1a4-5ab6737df658)

4. Полученный докинг

![image](https://github.com/user-attachments/assets/f29010e3-6163-44ba-b933-80b0b6253c68)



