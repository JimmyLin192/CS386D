
scripts=generator/generator.py run_sql.sh
sql_scripts=load Q1 Q2 Q3 schemas

push:
	git add $(scripts) $(sql_scripts) README.md Makefile 
	git commit
	git push
