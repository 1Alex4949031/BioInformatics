# Задание 4

_Работу выполнял через **wsl**_

1. Скачал результат секвенирования (набор ридов) Escherichia coli [SRR31254081](https://www.ncbi.nlm.nih.gov/sra/?term=SRR31254081)
2. Скачал референсный геном [Escherichia coli K-12 MG1655](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/)
3. Установил программы **FastQC, bwa, samtools**:
- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc) — анализ качества данных секвенирования.
- [bwa](https://github.com/lh3/bwa) — инструмент для выравнивания ридов на референсный геном.
- [samtools](https://www.htslib.org/) — набор инструментов для работы с файлами форматов SAM/BAM (результаты выравнивания ридов).
4. Проверил качество данных с помощью FastQC и сохранил отчет SRR31254081_fastqc.html:
```
fastqc SRR31254081.fastq
```
5. Индексирование референсного генома с помощью bwa:
```
 bwa index GCA_000005845.2_ASM584v2_genomic.fna
```

```
[bwa_index] Pack FASTA... 0.05 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 1.69 seconds elapse.
[bwa_index] Update BWT... 0.03 sec
[bwa_index] Pack forward-only FASTA... 0.03 sec
[bwa_index] Construct SA from BWT and Occ... 0.70 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index GCA_000005845.2_ASM584v2_genomic.fna
[main] Real time: 3.234 sec; CPU: 2.515 sec
```
- Индексирование референсного генома с помощью BWA создаёт несколько вспомогательных файлов, которые используются для ускорения процесса выравнивания ридов на этот референсный геном.
6. Выравнивание ридов на референсный геном:

  Теперь, когда геном индексирован, можно выровнять риды из файлов FASTQ на референсный геном.
  
```
bwa mem GCA_000005845.2_ASM584v2_genomic.fna SRR31254081.fastq.gz | gzip -3 > aln-se.sam.gz
```
```
[M::bwa_idx_load_from_disk] read 0 ALT contigs
[M::process] read 69438 sequences (10000263 bp)...
[M::process] read 69428 sequences (10000035 bp)...
[M::mem_process_seqs] Processed 69438 reads in 6.778 CPU sec, 6.722 real sec
[M::process] read 68842 sequences (10000074 bp)...
[M::mem_process_seqs] Processed 69428 reads in 6.439 CPU sec, 6.382 real sec
[M::process] read 69510 sequences (10000164 bp)...
[M::mem_process_seqs] Processed 68842 reads in 6.487 CPU sec, 6.416 real sec ...
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem GCA_000005845.2_ASM584v2_genomic.fna SRR31254081.fastq.gz
[main] Real time: 183.093 sec; CPU: 186.203 sec
```
7. Преобразование в формат BAM и сортировка (samtools view)
```
samtools view -Sb aln-se.sam.gz > aln-se.bam
samtools sort aln-se.bam -o aln-se.sorted.bam
```
8. Оценка качества выравнивания с помощью samtools flagstat
```
samtools flagstat aln-se.sorted.bam > flagstat_report.txt
```

```
1878477 + 0 in total (QC-passed reads + QC-failed reads)
1866822 + 0 primary
0 + 0 secondary
11655 + 0 supplementary
0 + 0 duplicates
0 + 0 primary duplicates
1289280 + 0 mapped (68.63% : N/A)
1277625 + 0 primary mapped (68.44% : N/A)
0 + 0 paired in sequencing
0 + 0 read1
0 + 0 read2
0 + 0 properly paired (N/A : N/A)
0 + 0 with itself and mate mapped
0 + 0 singletons (N/A : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
```
- Результат работы находится в файле flagstat_output.txt
9. Написал script-report.sh (однако дополнительно удалил симовол возврата каретки)
```
sed -i 's/\r$//' /mnt/c/Bio/task-4/ncbi_dataset/ncbi_dataset/data/GCA_000005845.2/script-report.sh
```
```
bash /mnt/c/Bio/task-4/ncbi_dataset/ncbi_dataset/data/GCA_000005845.2/script-report.sh
```
- Получили сообщение **not OK**
10. Настройка фрейсоврка Prefect
- Установка Prefect
```
pip install prefect
```
- Создадим базовый python файл hello_world.py
- Запустим сервер фрейсворка Prefect
```
prefect server start
```
```
Switched to profile 'local'

 ___ ___ ___ ___ ___ ___ _____
| _ \ _ \ __| __| __/ __|_   _|
|  _/   / _|| _|| _| (__  | |
|_| |_|_\___|_| |___\___| |_|

Configure Prefect to communicate with the server with:

prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

View the API reference documentation at http://127.0.0.1:4200/docs

Check out the dashboard at http://127.0.0.1:4200
```
- Еще нужно прописать
```
$env:PREFECT_API_URL="http://127.0.0.1:4200/api"
```
- После запуска файла hello_world.py получим
```
20:06:42.479 | INFO    | prefect.engine - Created flow run 'competent-bee' for flow 'hello-world'
20:06:42.487 | INFO    | prefect.engine - View at http://127.0.0.1:4200/runs/flow-run/9e4d9dc5-5fe7-4d2e-9797-a7851966425d
Hello, World!
20:06:42.651 | INFO    | Flow run 'competent-bee' - Finished in state Completed()
```
![image](https://github.com/user-attachments/assets/7f7e73ef-c909-4c00-b42f-653983a541eb)
11. Проверим написаный скрип на python. Выполним скрипт на python. По итогу получим
```
10:32:14.109 | INFO    | prefect.engine - Created flow run 'marigold-seal' for flow 'quality-assessment-pipeline'
10:32:14.111 | INFO    | prefect.engine - View at http://127.0.0.1:4200/runs/flow-run/f0541288-8f95-4393-ba8a-81e196cc04f1
10:32:16.473 | INFO    | Task run 'run_flagstat-2de' - Finished in state Completed()
10:32:16.496 | INFO    | Task run 'parse_flagstat_output-1cd' - Finished in state Completed()
not OK
10:32:16.515 | INFO    | Task run 'evaluate_alignment-063' - Finished in state Completed()
10:32:16.554 | INFO    | Flow run 'marigold-seal' - Finished in state Completed()
```
![image](https://github.com/user-attachments/assets/0235db5a-25b0-4774-8ceb-7009c551b7bc)
![image](https://github.com/user-attachments/assets/cf618cc7-ca96-426a-8cf4-9c3c97e89e30)




