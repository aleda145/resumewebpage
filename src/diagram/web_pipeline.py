from diagrams import Diagram
from diagrams.custom import Custom

from diagrams.onprem.ci import Droneci
from diagrams.onprem.network import Traefik
from diagrams.onprem.vcs import Github

from diagrams.programming.framework import Angular

with Diagram("Web Pipeline", show=False):
    angular = Angular("Web app")
    drone = Droneci("Drone")
    watchtower = Custom("WatchTower", "./logos/watchtower.png")
    github = Github("Github")
    dockerhub = Custom("", "./logos/dockerhub.png")
    traefik = Traefik("Traefik reverse proxy")
    traefik >> angular >> github >> drone >> dockerhub >> watchtower >> traefik
