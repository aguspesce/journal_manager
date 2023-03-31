# Journal manager

The Journal Manager is a custom command-line tool developed using Python that
helps manage and organize weekly tasks and activity logs across multiple projects.

It is based on low-friction task management system from
[https://github.com/CoralineAda/lftm](https://github.com/CoralineAda/lftm), 
which ensures that users can easily organize their tasks and projects while 
keeping track of their progress.

## Folder structure

Here is an example of the folder structure:

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

The Journal Manager requires the following dependencies:

- Datetime
- click
- pathlib
- Neovim as test editor (you can change it)

## How to use

To use the Journal Manager, follow these steps:

1. Open the `journal/journal.py` file, and locate the global variable  PATH_JOURNAL. Change its value to the path where you want to save your journal files.
2. Install all the necessary dependencies.
3. Use the Makefile to install the Journal Manager using the following command:
```
make install
```

Now, you can use the Journal Manager from the terminal by typing :
```
journal
```

To see the different options available with the Journal Manager, type the following command:
```
journal --help
```

## License

The source code is distributed under the
[BSD 3-clause License](https://opensource.org/licenses/BSD-3-Clause)
