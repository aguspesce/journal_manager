# Journal manager

Journal manager developed in Python to help me to organize my week's tasks and
have a log file with my activities in different projects.

It is based on low-friction task management system from
[https://github.com/CoralineAda/lftm](https://github.com/CoralineAda/lftm)

## Folder structure

For example:

```
HOME
|- Documentos
    |- journal
        |- 2022
            |- projects
            |   |- projec_name_1.md
            |   |- project_name_2.md
            |- tasks
                |- 2022-11-07.md
                |- 2022-11-14.md
```

## Dependencies

- Datetime
- click
- pathlib
- nvim as test editor (you can change it).
- mypy to check the type annotation.

## How to use it

Into `journal/journal.py` you mast to change the global variable `PATH_JOURNAL`
with the path where you want to save the journal files.

Use the Makefile to install it using `pip`:

```
make install
```

Now, you can use the journal manager from the terminal typing:

```
journal
```

## License

The source code is distributed under the
[BSD 3-clause License](https://opensource.org/licenses/BSD-3-Clause)
