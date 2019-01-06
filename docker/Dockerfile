FROM centos

RUN yum install -y python python-matplotlib-qt4 PyQt4-devel
RUN yum groupinstall -y "Development Tools"
RUN yum install -y  sudo cmake net-tools iproute

ENV USERNAME danielew
RUN useradd -m $USERNAME && \
    echo "$USERNAME:password" | chpasswd && \
    usermod --shell /bin/bash $USERNAME && \
    usermod -aG wheel $USERNAME && \
    usermod --uid 1000 $USERNAME && \
    groupmod --gid 1000 $USERNAME

ADD . /tmp/PyPlot
RUN cd /tmp/PyPlot/bin/debug && \
    ./configure && \
    make && \
    make install

CMD /bin/bash

