from diagrams import Diagram, Cluster

from diagrams.onprem.ci import Droneci
from diagrams.onprem.network import Traefik
from diagrams.onprem.vcs import Github

from diagrams.programming.framework import Angular
from diagrams.onprem.workflow import Airflow

from diagrams.elastic.elasticsearch import Elasticsearch, Beats, Kibana, LogStash

from diagrams.custom import Custom

with Diagram("Home Server Architecture", show=False):
    github = Github("Github")
    dockerhub = Custom("", "./logos/dockerhub.png")
    with Cluster("Docker"):
        watchtower = Custom("WatchTower", "./logos/watchtower.png")
        angular = Angular("Web app")
        drone = Droneci("Drone")
        jellyfin = Custom("Jellyfin", "./logos/jellyfin.png")
        portainer = Custom("", "./logos/portainer.png")
        grafana = Custom("", "./logos/grafana.png")
        superset = Custom("", "./logos/superset.png")

        angular >> github >> drone >> dockerhub >> watchtower

        watchtower >> angular

        traefik = Traefik("Traefik reverse proxy")
        traefik >> angular
        traefik >> drone
        traefik >> jellyfin
        traefik >> portainer
        traefik >> grafana
        traefik >> superset

        monitoring >> timescaledb
        
        timescaledb >> grafana
        timescaledb >> superset
        mumble = Custom("Mumble", "./logos/mumble.png")
        mumble
