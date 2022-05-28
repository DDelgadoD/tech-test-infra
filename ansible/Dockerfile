FROM debian:11
LABEL Name=ansible Version=0.0.1

# Install prerequisities for Ansible
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
  apt-get install -y python3-pip sshpass openssh-client libhdf5-dev libssl-dev libffi-dev && \
  rm -rf /var/lib/apt/lists/*

# Install ansible
RUN pip3 install --upgrade pip && \
  pip install ansible

# Creating dirs and updating hosts
RUN mkdir /ansible && \
  mkdir -p /etc/ansible && \
  mkdir /ssh

# Selecting working dir
WORKDIR /ansible

# Copy configuration files into the image
COPY playbook.yml /ansible
COPY hosts /etc/ansible/hosts
COPY rsa /ssh 
COPY rsa.pub /ssh


# Copy rsa keys for the ssh connection
RUN eval `ssh-agent -s` && ssh-add /ssh/rsa

# Run ansible to configure things
RUN ansible-playbook /ansible/playbook.yml

