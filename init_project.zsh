git remote remove origin
python3 -m venv ./venv;
source venv/bin/activate
pip3 install strictyaml
pip3 install pyDAL
pip3 install pytest
pip3 install pytest-tornasync
python3 -m pytest tests_project
