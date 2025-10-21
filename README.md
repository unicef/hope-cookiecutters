# HOPE Cookiecutter Templates


Powered by Cookiecutter, this repo contains a list of templates used by the HOPE ecosytem:
Each templated is into its own `TEMPLATE_FOLDER`

- django-project     : Template for Django based system within HOPE
- django-application : Template for reusable Django application
- python-library     : Generic python library
 

### How to use it 

```bash
    
    cookiecutter gh:unicef/hope-cookiecutters  --directory <TEMPLATE_FOLDER> --output-dir <my-projects-dir>
    
```

### Contribute to the project


```shell
    
    git clone https://github.com/unicef/hope-cookiecutters.git
    cd <TEMPLATE_FOLDER>
    make build  # build the template ans store the output into cc_test_dir/
```
