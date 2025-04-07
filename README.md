🧱 Detailed Implementation & Justification

✅ Step 1: Environment Setup
✔ What we did:
Airflow was installed using a pip.

 Create a workspace named ETL_Olist_Project.

 Python packages such as pandas and mysql-connector-python were installed.

🧠 Why:
An industry-standard solution for ETL process scheduling is Apache Airflow.

 A clear division of responsibilities is ensured by keeping all files in a single project directory.

 The necessary libraries provide database insertion (mysql-connector) and data wrangling (pandas).

✅ Step 2: Created the ETL Script (etl_olist_project.py)
✔ What we did:
One Python script was written that:

 reads several CSV files, including reviews, customers, order_items, and orders.

 carries out data aggregation and merger.

Calculates basic KPIs:

✅ Total Orders

✅ Total Unique Customers

✅ Average Review Score

✅ Total Items Sold

Inserts these KPIs into a MySQL database (olist_kpis table)

🧠 Why:
It encourages modularity to keep the logic in a separate script.

 Before connecting it to Airflow, you may test etl_olist_project.py on its own.

 The project's main tool for data transformation is this script.

✅ Step 3: Wrote the Airflow DAG (dags/olist_dag.py)
✔ What we did:
PythonOperator was used to create a DAG that called the run_etl() function from etl_olist_project.py.

basic DAG metadata defined: schedule_interval, start_date, and dag_id

Run_olist_etl = task

🧠 Why:
Data pipelines may be automatically scheduled and monitored thanks to DAGs.

PythonOperator allows us to run Python code directly without the need for shell wrappers.

The DAG serves as a link between the ETL procedure and Airflow.

✅ Step 4: Integrated MySQL via XAMPP
✔ What we did:
ran a local MySQL server using XAMPP.

built a database called olist_db.

created the olist_kpis table to hold the ETL process's results.

🧠 Why:
Local MySQL via XAMPP is quick, light, and simple to set up.

Keeping KPIs in a relational format enables dashboards, reports, and queries in the future.

✅ Step 5: Triggered DAG for Local Testing
✔ What we did:
attempted to launch the Airflow Webserver and Airflow Scheduler.

 OS-level problems were found.  (Native Windows does not completely support airflow.)

❗ Issue:
No module called 'pwd' blocked execution, among other errors

🔁 Our Solution:
decided that in order to fully integrate with Airflow, the project should be moved to WSL2 (Ubuntu).

🧠 Why:
The optimal operating system for Airflow is Linux.

 Without dual-booting, WSL2 provides a nearly native Linux experience on Windows.

 guarantees compatibility for every POSIX-compliant function that Airflow uses.

🔜 Next Steps (Phase 2 and Beyond)
Phase	Description
✅ Phase 1	Basic KPIs via ETL Script + Airflow DAG + MySQL
🧮 Phase 2	Advanced KPIs (CLV, Return Rate, Sales by Region)
🌐 Phase 3	Move Airflow to WSL2 + set up Scheduler & Web UI
📊 Phase 4	Build Dashboards using Python Dash or Tableau
☁️ Phase 5	Deploy ETL Flow (Optional: GCP, AWS, Azure)
