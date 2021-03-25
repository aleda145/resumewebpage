# diagram.py
from diagrams import Diagram, Cluster, Edge
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

with Diagram("Home Server Architecture", show=False):
    github = Github("Github")
    dockerhub = Custom("", "./logos/dockerhub.png")
    debian = Custom("Debian logs", "./logos/debian.png")
    with Cluster("Docker"):
        watchtower = Custom("WatchTower", "./logos/watchtower.png")
        logstash = LogStash("Logstash")
        beats = Beats("Filebeat")
        elastic = Elasticsearch("Elasticsearch")
        logstash >> elastic

        kibana = Kibana("Kibana")
        angular = Angular("Web app")
        drone = Droneci("Drone")
        jellyfin = Custom("Jellyfin", "./logos/jellyfin.png")
        jupyter = Custom("", "./logos/jupyter.png")
        concourse = Custom("Concourse", "./logos/concourse.png")
        jenkins = Custom("", "./logos/jenkins.png")
        mlflow = Custom("", "./logos/mlflow.png")
        portainer = Custom("", "./logos/portainer.png")
        angular >> github >> drone >> dockerhub >> watchtower
        airflow = Airflow("Airflow")
        airflow >> logstash
        elastic >> kibana
        watchtower >> angular
        traefik = Traefik("Traefik reverse proxy")
        traefik >> angular
        traefik >> drone
        traefik >> kibana
        traefik >> airflow
        traefik >> jellyfin
        traefik >> jupyter
        traefik >> concourse
        traefik >> jenkins
        traefik >> mlflow
        traefik >> portainer

        traefik_logs = Traefik("Traefik logs")
        traefik_logs >> beats
        beats >> elastic
        with Cluster("Other"):
            mumble = Custom("Mumble", "./logos/mumble.png")
            factorio = Custom("Factorio", "./logos/factorio.png")

            mumble - factorio

    debian >> logstash