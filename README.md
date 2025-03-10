# labss

***

## Лабораторная работа №1
1.Сначала переходим в папку lab1.

```shell
cd lab1
```
2.Создаем файлы ran.py, div.py, sqrt.py, errors.txt, logs.txt, output.txt с помощью команды touch.
3.Пишем код в файлах ran.py, div.py, sqrt.py.
4.Делаем питоновские файлы исполняемыми.

```shell
chmod +x ran.py
chmod +x div.py
chmod +x sqrt.py
```

5.Запускаем конвейер.

```shell
python ran.py | python div.py | python sqrt.py
```

## Лабораторная работа №2
1.Сначала переходим в папку lab2.

```shell
cd laba1
```

2.Создаем файлы greet.py, name.txt и error.txt с помощью команды touch.
3.Делаем питоновский файл исполняемым.

```shell
chmod +x greet.py
```

**Пример1**

Содержимое файла name.txt:

```text
Jack
michael
Kristina
321
Julia
```

```shell
./greet.py < name.txt 2> error.txt
```
```text
Nice to see you Jack!
Nice to see you Kristina!
Nice to see you Julia!
```
Все ошибки были сохранены в файле error.txt

**Пример 2**

```shell
./greet.py
```

```text
What's your name?
Julia
Nice to see you Julia!
What's your name?
Kirill
Nice to see you Kirill!
What's your name?
Alex
Nice to see you Alex!
What's your name?
67
Error: Name '67' needs to start uppercase!
What's your name?
^C
Goodbye!
```
