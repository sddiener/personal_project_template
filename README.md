
# Project Title

## Description
TODO: Brief description of what this project does.

## Quickstart
After setting up the project run the `main.py` function with the following input arguments, 
to do ... :
```
python src/main.py -x XXX -y YYY
```

## Setup and Installation

### Prerequisites
- Python 3.11
- Git (for cloning the repository)
- pre-commit (for enforcing code style guidelines)


### Setting Up the Virtual Environment
Create a virtual environment named `.venv`:
```
python3.11 -m venv .venv
```

Activate the virtual environment:

- On Windows:
  ```
  .venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source .venv/bin/activate
  ```

### Installing the current folder as a Python package

To be able to execute all the source code contained in the src module, one needs to install the current package as a Python module.
To do so, open a terminal and move to the root folder.
Then enter the following command :
`pip install -e .`

/!\ Be carefull not to forget the "." at the end of the command line since it specifies the path to the current folder (which is the path of the folder we want to instal as a Python package) !

### Installing Dependencies
Install the required packages:
```
pip install -r requirements.txt
```

### Installing and Configuring Pre-Commit Hooks
To ensure code formatting consistency, install pre-commit hooks:
```
pip install pre-commit
pre-commit install
```
This will set up `autopep8` to automatically format your code before each commit, according to the project's defined Python style guidelines.

### Running the Application
To run the main application:
```
python src/main.py [arguments]
```
Replace `[arguments]` with the appropriate command-line arguments for the application.

### Running Tests

#### Unittests
Run the tests located under `tests/unit` using pytest:
```
pytest tests/unit
```

## Branches

### Branch workflow
The repository will contain one main branches:

* `main`: the production branch


### Branch naming convension
In order to better identify and track branches and pull requests, branches should follow the following convevion:

{name_abrv}_{category}_{short_descripion}, e.g. `sdien_docs_add_readme`

More details, regarding the components, may be found below:
* `name_abrv`: should contain the first name of the first name, followed by the last name.
  In case the last name is too long, a shorter version should be used. 
  For example, _Georgios Chalkiopoulos_ would be written as `gchalkio`.
* `category`: each branch should, ideally, perform one small task and then be merged in the master or dev
  branch. We would like to avoid having branches that perform a lot of tasks, in order to be aligned 
  with Version Control best practices. The `category` is a brief description of this task. The 
  categories used in each case (subject to change) are :
  * `feature`: when implementing a new feature
  * `bugfix`: when working on a bug on the dev branch (which should usually be related to an issue)
  * `refactor`: when refactoring code
  * `docs`: when updating the documentation or adding useful reading material
* `short_description`: a short explanation of the purpose of the brancha


## Code Formatting
This project uses `autopep8` for code formatting. The code style is defined in the `setup.cfg` file, with a line length limit of 120 characters. 

To format code manually, run:
```
autopep8 --in-place --recursive src/ tests/
```

## Debugging in VS Code
To debug the application in Visual Studio Code, use the provided configuration in `.vscode/launch.json`. This allows you to debug `main.py` with predefined command-line arguments.

## Folder Structure
- `data/`: Data files used by the application.
- `docs/`: Docs and supporting notes/notebooks. Mostly contains Time Series Notes
- `logs/`: Location of log files for all modules
- `notebooks/`: Experimental scripts and notebooks.
- `src/`: Source code of the project.
- `tests/`: Test scripts for the application.

