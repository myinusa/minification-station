# Changelog

## [1.2.0](https://github.com/myinusa/minification-station/compare/v1.1.0...v1.2.0) (2024-10-03)


### Features

* filter files by programming language ([03c7188](https://github.com/myinusa/minification-station/commit/03c7188d10f1edb60da5c2932ce17f6ec3db5161))

## [1.1.0](https://github.com/myinusa/minification-station/compare/v1.0.0...v1.1.0) (2024-09-30)


### Features

* **constants.py:** add support for multiple programming languages by introducing `LANGUAGE_CONSTANTS`. ([cdc9ddc](https://github.com/myinusa/minification-station/commit/cdc9ddc07542788f17cbebae1b8bc8a65b743050))
* **main.py:** add handling for the new `--program_lang` argument in script initialization. ([cdc9ddc](https://github.com/myinusa/minification-station/commit/cdc9ddc07542788f17cbebae1b8bc8a65b743050))
* **traversal/directory_traversal.py:** update constructor to accept and use `program_lang` parameter from constants. ([cdc9ddc](https://github.com/myinusa/minification-station/commit/cdc9ddc07542788f17cbebae1b8bc8a65b743050))

## 1.0.0 (2024-09-28)


### Features

* **.gitignore:** add logs directory to ignore list ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/config:** add constants.py with default configurations ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/config:** add environment setup module ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/config:** add new args.py for argument parsing ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/logging:** add decorators for logging exceptions and function calls ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/logging:** add setup_logging.py for advanced logging configuration ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/processing:** add file_processor.py for file processing logic ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station/traversal:** add directory_traversal.py for file system navigation ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **minification_station:** add main module to orchestrate the application flow ([856f816](https://github.com/myinusa/minification-station/commit/856f8167e249f50a1d3575d7fb7103f7223a76d3))
* **poetry.lock:** add tqdm package with dependencies for progress tracking in file processing ([787e3fe](https://github.com/myinusa/minification-station/commit/787e3fe18a052d31b39f817506e4559895fa9520))
* release please workflow ([9e1509e](https://github.com/myinusa/minification-station/commit/9e1509e727100698de79348c4775f47c73f860f8))


### Bug Fixes

* **minification_station/config/args.py:** remove default argument from output argument in parser ([787e3fe](https://github.com/myinusa/minification-station/commit/787e3fe18a052d31b39f817506e4559895fa9520))
* **minification_station/config/enviornment_setup.py:** correct the directory creation logging message ([787e3fe](https://github.com/myinusa/minification-station/commit/787e3fe18a052d31b39f817506e4559895fa9520))
* **minification_station/main.py:** validate directory before processing and update output path ([787e3fe](https://github.com/myinusa/minification-station/commit/787e3fe18a052d31b39f817506e4559895fa9520))
* **minification_station/processing/file_processor.py:** change handling of output file to use Path object and adjust log message ([787e3fe](https://github.com/myinusa/minification-station/commit/787e3fe18a052d31b39f817506e4559895fa9520))
