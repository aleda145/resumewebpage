# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from diagrams.onprem.ci import Droneci
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Traefik
from diagrams.onprem.vcs import Github

from diagrams.programming.framework import Angular


from diagrams.custom import Custom


with Diagram("Web Pipeline", show=False):
    watchtower = Custom("WatchTower", "./logos/watchtower.png")
    dockerhub = Custom("dockerhub", "./logos/dockerhub.png")

    Angular("web") >> Github("github") >> Droneci("drone") >> dockerhub >> watchtower

