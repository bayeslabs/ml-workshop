#!/bin/bash -ex
{ set +x; } 2>/dev/null

chechAndInstallDocker() {
    if [ -z "$(which docker)" ]; then
        echo "Docker is not installed. Please install it first."
        read -p 'Do you want to install Docker? <yes/no> :  ' uservar
        if [ "$uservar" == "yes" ]; then
            curl -fsSL https://get.docker.com -o get-docker.sh
            sh get-docker.sh
            sudo usermod -aG docker $USER
            sudo systemctl enable docker
            sudo systemctl start docker
        else
            echo "Please install Docker first."
            exit 1
        fi
    else
        echo "Docker is installed."
    fi
}

chechAndInstallDocker