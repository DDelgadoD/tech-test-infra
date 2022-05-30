FROM debian:11
LABEL Name=ansible Version=0.0.1
ARG USERNAME=admin

# Install prerequisities for Ansible
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
  apt-get install -y python3-pip sshpass openssh-client libhdf5-dev libssl-dev libffi-dev && \
  rm -rf /var/lib/apt/lists/*

# Install ansible
RUN pip3 install --upgrade pip && \
  pip install ansible

# Creating dirs and updating hosts
RUN mkdir -p /etc/ansible
COPY hosts /etc/ansible/hosts
RUN useradd -ms /bin/bash $USERNAME

USER $USERNAME
RUN mkdir /home/$USERNAME/ansible

# Selecting working dir
WORKDIR /home/$USERNAME/ansible

# Copy configuration files into the image
COPY playbook.yml /home/$USERNAME/ansible
COPY vars.yml /home/$USERNAME/ansible
COPY rsa /home/$USERNAME/.ssh/
COPY rsa.pub /home/$USERNAME/.ssh/

# Run ansible to configure things
RUN ansible-playbook /home/$USERNAME/ansible/playbook.yml && \
  ssh-copy-id -i /home/$USERNAME/.ssh/rsa.pub david@192.168.122.234


