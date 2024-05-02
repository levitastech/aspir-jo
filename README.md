


# aspir-jo: Python JORADP Downloader
### Python joradp Downloader Ver 2.7.2-b Copyright 2023-2024

aspir-jo is a Python-based command-line application that allows you to download PDF files from the archives of the JORADP (Journal Officiel de la République Algérienne Démocratique et Populaire).

## Introduction

The JORADP is the official journal of the Algerian government, containing important publications such as laws, decrees, and official announcements. This application provides a convenient way to download and archive PDF files from the JORADP website, making it easier to access and search these publications.

## Description

The aspir-jo application is designed to be user-friendly and flexible. It offers a range of options to customize the download process according to your specific needs. You can download publications for a particular year, a specific publication index within a year, or all publications from the available years.

Additionally, the application supports creating separate directories for each year, making it easier to organize and manage the downloaded PDF files.

## Functionality

The aspir-jo application offers the following main functionalities:

1. **Download All Publications**: Without any options specified, the application will download all available publications from the JORADP website, starting from the year 1962 up to the current year.

2. **Download Publications by Year**: You can specify a particular year using the `-y` or `--year` option, and the application will download all publications for that year.

3. **Download Specific Publication**: If you know the publication index (issue number) for a specific year, you can use the `-i` or `--index` option along with the `-y` or `--year` option to download that particular publication.

4. **Create Separate Directories**: By using the `-d` or `--directories` option, the application will create separate directories for each year, making it easier to organize the downloaded PDF files.

5. **Display Version and Copyright**: Use the `-v` or `--version` option to display the application's name, version, and copyright information.

6. **Display Help**: Use the `-h` or `--help` option to display the usage information and a brief description of each option.

## Options

The aspir-jo application supports the following command-line options:

- `-h`, `--help`: Print the usage information and a brief description of each option.
- `-v`, `--version`: Display the application's name, version, and copyright information.
- `-d`, `--directories`: Create separate directories for each year when downloading publications.
- `-y YYYY`, `--year YYYY`: Download all publications for the specified year (valid years: 1962 to the current year).
- `-i nnn`, `--index nnn`: Download a specific publication index for the given year (requires the `--year` option).

## Examples

Here are some examples of how to use the aspir-jo application:

1. Download all publications for the year 2022:
```
    python main.py --year 2022
```

2. Download publication index 125 for the year 2022:

``` 
    python main.py --year 2022 --index 125 
```

3. Create separate directories for each year and download all publications:
```
    python main.py --directories
```

4. Create separate directories for each year and download all publications for the year 2022:
```
    python main.py --directories --year 2022
```

5. Create separate directories for each year and download publication index 125 for the year 2022:
```
python main.py --directories --year 2022 --index 125
```

6. Display the application's version and copyright information:
```
    python main.py --version
```

7. Display the help information:
```
python main.py --help
```


## Information

- Author: Reda Medani
- Version: 2.7.2-b
- Copyright: 2023-2024
- License: [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl-3.0.html)

## Contributing

Contributions to the aspir-jo project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/levitastech/aspir-jo).

## Acknowledgments

This application was inspired by the need to easily access and archive important publications from the JORADP website. Special thanks to the developers of the Python libraries used in this project, including requests, pathlib, and argparse.

