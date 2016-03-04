
scripts=generator/generator.py run_sql.sh
sql_scripts=load Q1 Q2 Q3 schemas

push:
	git add $(scripts) $(sql_scripts) README.md Makefile 
	git commit
	git push

tar:
	tar czvf CS386D_Xin_XL5224.tar.gz $(scripts) $(sql_scripts) README.md Makefile report.pdf
