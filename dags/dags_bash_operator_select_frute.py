from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dag_bash_operator",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    t1_orange = BashOperator(
        task_id="/opt/airflow/plugins/select_fruit.sh ORANGE",
        bash_command="",
    )
    
    t2_avocado = BashOperator(
        task_id="t2_avocado",
        bash_command="/opt/airflow/plugins/select_fruit.sh AVOCADO",
    )

    t1_orange >> t2_avocado