# Container Managers

!!! info "Architectural Context"
    Detailed reference for Container Managers in the context of The Container Stack.

## Standard Reference

  - [A Practical Introduction to Container Terminology](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.alexellis.io: Building containers without Docker 🌟](https://blog.alexellis.io/building-containers-without-docker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [runc](https://github.com/opencontainers/runc) <span class='md-tag md-tag--info'>⭐ 13237</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [crun](https://github.com/containers/crun) <span class='md-tag md-tag--info'>⭐ 3933</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [Conmon](https://github.com/containers/conmon) <span class='md-tag md-tag--info'>⭐ 479</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerd - An open and reliable container runtime](https://github.com/containerd/containerd) <span class='md-tag md-tag--info'>⭐ 20746</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span>
  - [What is Podman and How Does it Compare to Docker?](https://build5nines.com/what-is-podman-and-how-does-it-compare-to-docker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes.io: Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerd.io](https://containerd.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cri-o.io](https://cri-o.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Podman.io](https://podman.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Intro to Podman](https://developers.redhat.com/blog/2018/08/29/intro-to-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [redhat.com: Be careful when pulling images by short name](https://www.redhat.com/en/blog/be-careful-when-pulling-images-short-name)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Podman and Buildah for Docker users 🌟](https://developers.redhat.com/blog/2019/02/21/podman-and-buildah-for-docker-users)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [podmain.io: Announcing Podman v2](https://podman.io/blogs/2020/06/29/podman-v2-announce.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Getting started with Podman](https://www.youtube.com/watch?v=Za36qHbrf3g)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Rootless containers with Podman: The basics](https://developers.redhat.com/blog/2020/09/25/rootless-containers-with-podman-the-basics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tecmint.com: How to Manage Containers Using Podman and Skopeo in RHEL 8](https://www.tecmint.com/manage-containers-using-podman-in-rhel)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Tutorial: Host a Local Podman Image Registry 🌟](https://thenewstack.io/tutorial-host-a-local-podman-image-registry)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fedoramagazine.org: Manage containers with Podman Compose](https://fedoramagazine.org/manage-containers-with-podman-compose)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Podman in Podman (Running a container within a container)](https://www.youtube.com/watch?app=desktop&v=OcHRWaC5tvY&feature=youtu.be&ab_channel=RedHat)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [wbhegedus.me: Configuring Podman for WSL2 🌟](https://wbhegedus.me/running-podman-on-wsl2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Using Podman Compose with Microcks: A cloud-native' API mocking and testing tool](https://developers.redhat.com/blog/2021/04/22/using-podman-compose-with-microcks-a-cloud-native-api-mocking-and-testing-tool)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tutorialworks.com: How to Start Containers Automatically, with Podman and' Systemd](https://www.tutorialworks.com/podman-systemd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Podman 3 and Docker Compose - How Does the Dockerless Compose Work?' 🌟](https://www.youtube.com/watch?v=15PFfjuxtvM&ab_channel=mkdev)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fedoramagazine.org: Use Docker Compose with Podman to Orchestrate Containers' on Fedora Linux](https://fedoramagazine.org/use-docker-compose-with-podman-to-orchestrate-containers-on-fedora)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Run a Linux virtual machine in Podman](https://opensource.com/article/21/7/linux-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Transitioning from Docker to Podman 🌟](https://developers.redhat.com/blog/2020/11/19/transitioning-from-docker-to-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pythonspeed.com: Using Podman with BuildKit, the better Docker image builder' 🌟](https://pythonspeed.com/articles/podman-buildkit)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devopscube.com: Podman Tutorial For Beginners: Step by Step Guides 🌟](https://devopscube.com/podman-tutorial-beginners)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetespodcast.com: Podman, with Daniel Walsh and Brent Baude](https://kubernetespodcast.com/episode/164-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Get podman up and running on Windows using Linux](https://opensource.com/article/21/10/podman-windows-wsl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [darumatic.com: Podman - Introduction 🌟](https://darumatic.com/blog/podman_introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iongion.github.io: Podman Desktop Companion 🌟](https://iongion.github.io/podman-desktop-companion)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [imaginarycloud.com: Podman vs Docker: What are the differences?](https://www.imaginarycloud.com/blog/podman-vs-docker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Run containers on Linux without sudo in Podman](https://opensource.com/article/22/1/run-containers-without-sudo-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Containers without Docker (podman, buildah, and skopeo)](https://dev.to/cedricclyburn/containers-without-docker-podman-buildah-and-skopeo-1eal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Podman Desktop](https://podman-desktop.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Podman expands to the Desktop](https://developers.redhat.com/articles/2022/10/24/podman-expands-desktop)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [sherifabdlnaby/kubephp](https://github.com/sherifabdlnaby/kubephp) <span class='md-tag md-tag--info'>⭐ 455</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iximiuz.com: In Pursuit of Better Container Images: Alpine, Distroless,' Apko, Chisel, DockerSlim, oh my!](https://iximiuz.com/en/posts/containers-making-images-better)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Introducing the Red Hat Universal Base Image 🌟](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [What is Red Hat Universal Base Image?](https://developers.redhat.com/blog/2019/10/09/what-is-red-hat-universal-base-image)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [RH Universal Base Image FAQ](https://developers.redhat.com/articles/ubi-faq/#resources)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ubi-micro: RHEL tiny images to build containers 🌟](https://github.com/fatherlinux/ubi-micro)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: How to pick the right container base image](https://developers.redhat.com/blog/2021/04/13/how-to-pick-the-right-container-base-image)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Docker, Kaniko, Buildah](https://itnext.io/docker-kaniko-buildah-209abdde5f94)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kubesimplify.com: Getting started with ko: A fast container image builder' for your Go applications](https://blog.kubesimplify.com/getting-started-with-ko-a-fast-container-image-builder-for-your-go-applications)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Buildah.io](https://buildah.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/containers/buildah](https://github.com/containers/buildah) <span class='md-tag md-tag--info'>⭐ 8795</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [developers.redhat.com: Getting started with Buildah](https://developers.redhat.com/blog/2021/01/11/getting-started-with-buildah)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: How to live without Docker for developers - Part 1 | Migration' from Docker to Buildah and Podman](https://www.youtube.com/watch?app=desktop&v=Fl0iLoAMdzc&ab_channel=AndrewMalkov)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Skopeo](https://github.com/containers/skopeo) <span class='md-tag md-tag--info'>⭐ 10891</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>

## DevSecOps

### CICD Pipeline Security

#### Podman

  - [Build trusted pipelines/Guards with Podman containers](https://www.redhat.com/en/blog/using-container-technology-make-trusted-pipeline)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Evaluates strategies for building rootless, secure continuous integration pipelines using Red Hat's Podman. Contrasts Podman's daemonless security with Docker's privileged execution models to prevent pipeline takeover attacks.
## Infrastructure

### Containerization

#### Kernel Internals

  - [Controlling Process Resources with Linux Control Groups (cgroups)](https://labs.iximiuz.com/tutorials/controlling-process-resources-with-cgroups) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A deep, interactive laboratory walk-through demonstrating how Linux Control Groups (cgroups) throttle and isolate system resources. Crucial baseline knowledge for understanding container limits in Kubernetes.
## Observability

### Logging

#### Command Line Tools

  - [bul: Interactive TUI for Exploring Kubernetes Container Logs](https://github.com/ynqa/bul) <span class='md-tag md-tag--info'>⭐ 16</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An interactive Terminal User Interface (TUI) written in Go for streaming and searching Kubernetes container logs. Grounding suggests that development has stalled (inactive for over 4 years), so while technically functional for local dev, tools like Stern or K9s are preferred in enterprise environments.

---
💡 **Explore Related:** [Kubernetes Alternatives](./kubernetes-alternatives.md) | [Kubernetes Bigdata](./kubernetes-bigdata.md) | [Noops](./noops.md)

