# Microtask 1:
Create a Python script to execute Perceval via its Python interface using the Git and GitHub backends. Feel free to select any target repository.

## Git Backend

* `git_backend.py` is the script to execute Perceval on Git backend.

* Script supports dumping extracted JSON data to a file or printing it to terminal.

* From date and to date is also supported.

* A few parameters for running the script are defined below.

```
-r, --repo = "Git repository URI"
-p, --gitpath = "Gitpath of the repository"
-d, --create_dump = "y/n for creating JSON data dumps"
```

Sample usage
```
python3 git_backend.py -r https://github.com/imnitishng/grimoirelab-perceval-mozilla -p grimoirelab-perceval-mozilla -d y
```

2. Prepare a virtualenv to install and manage all packages separate from other projects. 
```
$ python3 -m venv ~/venvs/grimoirelab
$ source ~/venvs/grimo/bin/activate
```
The above commands create and activate a virtual environment in the `~/venvs/grimoirelab` directory.

3. Install all the requirments for Perceval.
```
$ pip3 install -r requirements.txt
$ pip3 install -r requirements_tests.txt
$ pip3 install -e .
```

4. Open Perceval using PyCharm and set interpreter as the virtual environment created above.
	
	<img src="./images/perceval_set.png" width="800" alt="Perceval set">
 
5. Run Perceval for the first time on the `perceval` repository using the command.
   
	`perceval github grimoirelab perceval --sleep-for-rate`

	<img src="./images/pycharm_run.png" width="800" alt="Run">

   Additional arguments for running perceval can be found on the [grimoirelab tutotial](https://chaoss.github.io/grimoirelab-tutorial/perceval/github.html) page