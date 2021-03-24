# diagram.py
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from diagrams.onprem.ci import Droneci
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Traefik
from diagrams.onprem.vcs import Github

from diagrams.programming.framework import Angular
from diagrams.onprem.workflow import Airflow

from diagrams.elastic.elasticsearch import Elasticsearch, Beats, Kibana, LogStash

from diagrams.custom import Custom

with Diagram("Home Server", show=False):
    github = Github("github")
    dockerhub = Custom("dockerhub", "./logos/dockerhub.png")
    with Cluster("Docker"):
        watchtower = Custom("WatchTower", "./logos/watchtower.png")

        logstash = LogStash("Logstash")
        elastic = Elasticsearch("Elasticsearch")
        logstash >> elastic
        with Cluster("Traefik"):
            kibana = Kibana("Kibana")
            angular = Angular("web")
            drone = Droneci("drone")
            angular >> github >> drone >> dockerhub >> watchtower
            airflow = Airflow("")
            airflow >> logstash
            elastic >> kibana
        traefik = Traefik()
        traefik >> logstash
        traefik >> angular
        traefik >> drone
        traefik >> kibana
        traefik >> airflow
