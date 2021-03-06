# Лабораторная работа #1: Test-Driven Development

## Цели

  1. Освоить практику разработки Test-Driven Development (TDD).
  1. Освоить "гибкую" практику ОО дизайна, рассмотренную в лекциях "TDD", "Чистый код", "Рефакторинг".
  1. Ознакомиться с практикой непрерывной интеграции.

## Задачи

  1. Доустановить инструменты разработки в виде IDE (рекомендуется PyCharm Community Edition) и все необходимые зависимости для проекта.
  1. Разработать Python-модуль с основной логикой приложения согласно практике TDD. Классы должны быть "грамотно" спроектированы, должны выполняться рекомендации из лекции "Чистый код".
  1. Прислать результаты в виде пулл-реквеста, и добиться прохождения всех проверок на системе непрерывной интеграции Travis CI.

## Типичные ошибки

  1. Написание кода вперед тестов. __Следует строго следовать TDD__, иначе это будет сразу видно. В таком случае лабу придется переделывать.
  1. Если тестов будет мало, их придется писать, пока их не станет по ~3 штуки на каждый публичный метод. Поэтому лучше сразу пишите по TDD.
  1. Не нужно делать коммиты файлов с бинарными сборками и других временных файлов от IDE.

## Детальные инструкции

### Первичная настройка

  1. Просьба следовать процессу [GitHub Flow][github-flow]. Это подразумевает, что разработку вы ведете в отдельной ветке Git. Просьба создать ветку, дав ей содержательное имя, например `lab1-tdd-triangle`. Кроме того, если к вашем коду будут поступать замечания, то просьба не создавать новые ветки и пулл-реквесты, а использовать те же самые. Так, при `git push` коммитов в ветку `lab1-tdd-triangle` на вашем форке, пулл-реквест обновится автоматически.
  1. Первым делом полезно обновить коды из центрального репозитория ([upstream][upstream]). Когда вы скачаете коды и сделаете их `merge` в свой `master`, можно будет создавать ветку `lab1-tdd-triangle` и продолжать в ней работу. Вот примерные команды, которые вы должны использовать:

      ```bash
        $ cd agile-course-practice
        $ git remote add upstream https://github.com/UNN-ITMM-Software/agile-course-practice-template/
        $ git fetch upstream
        $ git checkout master
        $ git rebase upstream/master
        $ git checkout -b lab1-tdd-triangle
      ```
  1. Теперь нужно установить IDE, запустить все тесты и убедиться, что они проходят.

     - Если вы планируете использовать PyCharm (рекомендуется), то Вам будет 
     предложено установить зависимости из файла *requirements.txt*, что и нужно сделать.

     - Аналогично, если вы планируете использовать текстовый редактор, подготовьте 
     виртуальное окружение для работы, установите зависимости. Команды для Windows:
       ```powershell
       PS python -m venv venv
       PS ./venv/Scripts/activate.bat
       PS pip install -r requirements.txt
       ```

## Выполнение лабораторной

  1. Далее вы можете начинать работу над своим проектом. Для простоты можно
     скопировать проект `fraction`, и переиспользовать его
     структуру, переименовав все под свою лабораторную. Конечно, все Python-файлы
     придется удалить и написать заново. Скопированный проект можно
     импортировать в IDE и собственно приступить к разработке своего компонента.
     - __Внимание:__ просьба все свои лабораторные выполнять в той же директории
       со своим именем, развивая и наращивая проект. Папки с примерами с
       суффиксами (вида `kirill-kornyakov-lab1`) создаются лишь для того, чтобы
       вы видели разницу между лабораторными. Вы же должны работать в одной
       папке.
  1. Свой подпроект необходимо добавить в общий проект и оформить его как python-модуль.
     Добавьте пустой файл `__init__.py` в папку с подпроектом, и в папки с его модулями.
  1. Собственно далее вы должны разработать свой класс, решающий поставленную
     задачу, согласно практике TDD. Перед этим рекомендуется освежить в памяти
     [ключевые рекомендации][tddcast].
     - __Настоятельно рекомендуется__ соблюдать все рекомендации практики:
       создание теста до кода, маленькие итерации (думаете больше 5 минут -
       пишите вспомогательный класс или метод), периодический рефакторинг кода и
       тестов.
     - __На каждый метод у вас должно в среднем не менее 3 тестов__, пара smoke
       тестов (просто на корректную работу), затем граничные значения и
       неадекватные/недопустимые аргументы.
     - Кроме того, огромная просьба следить за чистотой кода, понятностью имен и
       следованию [PEP8][codestyle].

## Интеграция

  1. Когда все будет готово, нужно будет прислать пулл-реквест и убедиться, что
     он [зеленый][agile-travis]. Если это не так, просьба самостоятельно
     разрешить все проблемы. Код будет рецензироваться только если пулл-реквест
     проходит все тесты. Среди прочего, автоматически будет проверяться стиль
     кодирования.
  1. Когда ваш pull request станет зеленым, начинается фаза code review.
     - Как обычно, сперва нужно пройти ревью у двоих однокурсников и получить их
       :+1:. Если в свою очередь вы рецензируете чей-то код, то делайте это
       тщательно и ответственно. Проверяйте стиль кодирования, полноту
       тестов, удобство API и дизайна, понятность кода. Все замечания
       высказывайте автору.
     - Полученные замечания нужэно своевременно устранять, и это нужно делать в
       той же ветке и в том же пулл-реквесте. Когда все замечания будут
       устранены (чаще всего они на чистоту кода), нужно пригласить к рецензии
       преподавателей.

Как обычно, лабораторная считается засчитанной в тот момент, когда коды
вливаются в ветку `master` центрального репозитория.

<!-- LINKS -->

[github-flow]:  http://scottchacon.com/2011/08/31/github-flow.html
[agile-travis]: https://travis-ci.com/github/UNN-ITMM-Software/agile-course-practice-python/pull_requests
[upstream]:     https://github.com/UNN-ITMM-Software/agile-course-practice-template/
[codestyle]:    https://www.python.org/dev/peps/pep-0008/
[tddcast]:      http://www.youtube.com/watch?v=lDdJYid8NpE
