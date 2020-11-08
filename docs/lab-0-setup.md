# Лабораторная работа #0: Настройка окружения

* [Цели](#цели)
* [Задачи](#задачи)
* [Детальные инструкции](#детальные-инструкции)
    * [Конфигурация Python окружения](#конфигурация-python-окружения)
    * [Получение исходников](#получение-исходников)
    * [Реализация нескольких простых тестов](#реализация-нескольких-простых-тестов)
    * [Ревью кода](#ревью-кода)

-------------------------

## Цели

1. Ознакомиться с общей процедурой приема лабораторных работ.
1. Познакомиться с инфраструктурой GitHub + Travis CI и принятым там процессом разработки (workflow).

## Задачи

1. Разверните необходимое окружение:
    - Git, pyenv, Python 3.7.3, Tcl/Tk, PyCharm или текстовый редактор.
1. Получите [проект-шаблон][upstream] и протестируйте его локально:
    - Создайте свой форк [центрального репозитория][upstream], а также включите для него тестирование на TravisCI.
    - Клонируйте проект к себе на машину и запустите все имеющися тесты и проверки (flake8).
    - Также, запустите графическое приложение, убедившись, что оно работает, а значит все необходимые зависимости (Tcl/Tk) присутствуют.
1. Реализуйте простейшие тесты на модуль `fraction` и пришлите пробный pull request:
    - Добавьте новый файл со своими тестами для модуля `fraction`.
    - Пошлите свою лабораторную в виде pull request на GitHub и пройдите ревью кода. Сначала вам необходимо получить два одобрения (`+1`) от сокурсников, затем от преподавателя.

В принципе, если все это понятно, можно сразу приступать к работе и дальше не читать. Детальные инструкции призваны помочь в том случае, если описанный цикл работы является для вас новым.

Вот, для примера, команды, которые должны привести к успеху на macOS

```bash
$ pyenv uninstall 3.7.3
$ env   PATH="$(brew --prefix tcl-tk)/bin:$PATH"   LDFLAGS="-L$(brew --prefix tcl-tk)/lib"   CPPFLAGS="-I$(brew --prefix tcl-tk)/include"   PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"   CFLAGS="-I$(brew --prefix tcl-tk)/include"   PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'"   pyenv install 3.7.3
$ pyenv versions
$ pyenv global 3.7.3
$ python -V
$ python -m tkinter -c 'tkinter._test()'
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ nosetests -x --with-coverage code/*
$ flake8 --max-line-length=110 code
```

Если работаете под Windows, достаточно создать(или добавить значение) переменную среды PYTHONPATH, значение - пусть до папки *code* данного проекта.
PyCharm сам предложит установить все необходимые зависимости. 

## Детальные инструкции

### Конфигурация Python окружения

1. Установите себе Python 3.7.3 c поддержкой Tcl/Tk. Разумнее всего это сделать с использованием pyenv, чтобы окружения не мешали друг другу.
    - На macOS должна помочь следующая инструкция: https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos/60469203#60469203
1. Установите себе IDE для работы по выбору, рекомендуется использовать PyCharm или обычный текстовый редактор + консоль.
1. Критерием успеха на этом этапе должно являться то, что следующая команда выведет небольшое графическое окошко.

    ```bash
    $ python -m tkinter -c "tkinter._test()"
    ```

### Получение исходников

1. Если у вас еще нет GitHub аккаунта, то зарегистрируйтесь там. Предпочтительно использование логина, из котого понятно ваше имя.

1. Установите и настройте себе Git, используя инструкции например [отсюда][help-git]. При необходимости можно посмотреть [запись][gitcast] демонстрации Git + GitHub.

1. Создайте форк [проекта][upstream], затем клонируйте созданный `origin` репозиторий (это ваш форк) к себе на рабочую машину. Все необходимые инструкции можно найти [здесь][help-fork].
    - В результате у вас должны быть объявлены и `origin` и `upstream` репозитории, стоит убедиться в правильности путей при помощи команды `$ git remote -v`.

    ```bash
    $ git clone https://github.com/YOUR_GITHUB_NAME/agile-course-practice-python
    $ git remote add upstream https://github.com/UNN-ITMM-Software/agile-course-practice-python
    $ git remote -v
    ```

1. Также, включите тестирование своего форка на TravisCI, чтобы производить тестирование своих лабораторных в контексте репозитория `origin`, и не ждать в общей очереди на `upstream`.

### Реализация нескольких простых тестов

1. Создайте новую ветку, в которой вы будете работать над лабораторной:

    ```bash
    $ cd agile-course-practice-python
    $ git checkout -b surname-name-lab1
    ```

1. Запустите тестирование локально, и убедитесь, что проект успешно проходит проверки:

    ```bash
    $ python -V # Ответом должно быть "Python 3.7.3"
    $ python -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ nosetests -x --with-coverage code/*
    $ flake8 --max-line-length=110 code
    ```

1. Создайте файл и реализуйте в нем два или более простых теста на класс `fraction`. Когда закончите, нужно сделать локальный коммит в Git:

    ```bash
    $ git add code/fraction/model/test_YOUR_NAME.md
    $ git commit -m "Added more unit tests"
    ```

1. Далее сделайте `git push` в свой форк проекта. Также, для целей тестирования, стоит обновить состояние `origin/master` до состояние `upstream/master` (делайте это периодически, чтобы как можно быстрее узнавать о потенциальных конфликтах и проблемах, в связи с тем, что `upstream/master` ушел вперед).

    ```bash
    $ git push origin HEAD
    $ git remote update
    $ git push origin/master upstream/master
    ```

1. Затем стоит сделать [pull-request][help-pr] в `origin/master` с целью тестирования. Первым делом необходимо убедиться, что успешно прошло тестирование на [Travis CI][travis] (только ссылка для вашего форка будет уже другая). Вероятность того, что что-то пойдет не так, невелика (в том случае, если локально у вас все отработало), но ниже приведены инструкции на тот случай, если что-то нужно поправить.

    ```bash
    # Редактирование исходников
    $ git commit -a -m "Fixing issues"
    $ git push origin HEAD
    ```

Когда тестирование пройдет, лучше не вливать pull request, а просто его закрыть. Состояние `origin/master` лучше менять только обновлениями из `upstream/master`.

### Ревью кода

1. После этого стоит сделать [pull-request][help-pr] в `upstream/master` с целью финальных проверок и интеграции. В названии pull-request нужно указать свою фамилию и номер лабораторной, например _"Корняков - Лабораторная работа #0"_.

1. Далее необходимо пройти ревью кода от двух своих сокурсников. Пригласите их к дискуссии, дабавив в pull request комментарий вида `@github-name` (например `@kirill-korniakov`).

1. Если будут замечания к вашему коду, вам нужно добавлять коммиты в свою ветку, и пулл-реквест будет автоматически обновляться.

1. Формально вам нужно получить два комментария вида :+1: (пишется как `:+1:`). Наличие такого значка фактически означает одобрение коллегой ваших изменений. Затем необходимо аналогичным образом пригласить одного из преподавателей и пройти окончательное ревью.

После прохождения ревью код будет влит в основную ветку `master`, и установочную лабу можно считать завершенной.

<!-- LINKS UPDATABLE -->

[topics]:   https://docs.google.com/spreadsheets/d/1Pt9i-UGUiFG8_tjnUjxmCqVjP9VHG9GJc1LNZQeGU_4/edit#gid=489721713

<!-- LINKS PERMANENT -->

[upstream]: https://github.com/UNN-ITMM-Software/agile-course-practice-python
[travis]:   https://travis-ci.com/github/UNN-ITMM-Software/agile-course-practice-python/pull_requests
[gitcast]:  http://www.youtube.com/playlist?list=PLSzOhsr5tmhrgV7u7CSzX4Ki1a9r0AKzV

[help-git]:  https://help.github.com/articles/set-up-git
[help-fork]: https://help.github.com/articles/fork-a-repo
[help-pr]:   https://help.github.com/articles/using-pull-requests
[gfm]:       https://help.github.com/articles/github-flavored-markdown
