#!/bin/bash

# Запускаем samtools flagstat и сохраняем результат
samtools flagstat aln-se.sorted.bam > flagstat_output.txt

# Извлекаем процент выравнивания из результата
mapped_percentage=$(grep -oP '\d+\.\d+%' flagstat_output.txt | head -1 | tr -d '%')

# Пороговое значение качества
threshold=90.0

# Проверяем, соответствует ли результат порогу
if (( $(echo "$mapped_percentage >= $threshold" | bc -l) )); then
    echo "OK"
else
    echo "not OK"
fi
