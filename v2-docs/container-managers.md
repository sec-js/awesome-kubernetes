# Container Runtimes/Managers, Base Images and Container Tools. Podman, Buildah & Skopeo

!!! info "Architectural Context"
    Detailed reference for Container Runtimes/Managers, Base Images and Container Tools. Podman, Buildah & Skopeo in the context of The Container Stack.

## Standard Reference

  - [cri-o.io](https://cri-o.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Podman and Buildah for Docker users 🌟](https://developers.redhat.com/blog/2019/02/21/podman-and-buildah-for-docker-users)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [A Practical Introduction to Container Terminology](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.alexellis.io: Building containers without Docker 🌟](https://blog.alexellis.io/building-containers-without-docker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [runc](https://github.com/opencontainers/runc) <span class='md-tag md-tag--info'>⭐ 13237</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [crun](https://github.com/containers/crun) <span class='md-tag md-tag--info'>⭐ 3933</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [Conmon](https://github.com/containers/conmon) <span class='md-tag md-tag--info'>⭐ 479</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerd - An open and reliable container runtime](https://github.com/containerd/containerd) <span class='md-tag md-tag--info'>⭐ 20746</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span>
  - [What is Podman and How Does it Compare to Docker?](https://build5nines.com/what-is-podman-and-how-does-it-compare-to-docker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes.io: Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Docker](https://www.docker.com/products/container-runtime)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [containerd.io](https://containerd.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Podman.io](https://podman.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Intro to Podman](https://developers.redhat.com/blog/2018/08/29/intro-to-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [redhat.com: Be careful when pulling images by short name](https://www.redhat.com/en/blog/be-careful-when-pulling-images-short-name)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [podmain.io: Announcing Podman v2](https://podman.io/blogs/2020/06/29/podman-v2-announce.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Getting started with Podman](https://www.youtube.com/watch?v=Za36qHbrf3g)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Rootless containers with Podman: The basics](https://developers.redhat.com/blog/2020/09/25/rootless-containers-with-podman-the-basics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [tecmint.com: How to Manage Containers Using Podman and Skopeo in RHEL 8](https://www.tecmint.com/manage-containers-using-podman-in-rhel)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Tutorial: Host a Local Podman Image Registry 🌟](https://thenewstack.io/tutorial-host-a-local-podman-image-registry)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fedoramagazine.org: Manage containers with Podman Compose](https://fedoramagazine.org/manage-containers-with-podman-compose)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Podman: Getting Started](https://medium.com/javarevisited/podman-getting-started-e7fc06961994)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [oldgitops.medium.com: Setting up Podman on WSL2 in Windows 10 🌟](https://oldgitops.medium.com/setting-up-podman-on-wsl2-in-windows-10-be2991c2d443)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
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
  - [medium.com: Exploring Docker alternative — Podman](https://medium.com/techbeatly/exploring-docker-alternative-podman-14674c990311)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [darumatic.com: Podman - Introduction 🌟](https://darumatic.com/blog/podman_introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [iongion.github.io: Podman Desktop Companion 🌟](https://iongion.github.io/podman-desktop-companion)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [imaginarycloud.com: Podman vs Docker: What are the differences?](https://www.imaginarycloud.com/blog/podman-vs-docker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Run containers on Linux without sudo in Podman](https://opensource.com/article/22/1/run-containers-without-sudo-podman)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@raghavendraguttur: Podman Containers — Beginner’s Guide](https://medium.com/@raghavendraguttur/podman-containers-beginners-guide-830b931e66f4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [nilesh93.medium.com: Replacing Docker Desktop with Podman and Kind in MacOS](https://nilesh93.medium.com/replacing-docker-desktop-with-podman-and-kind-in-macos-c750581a3fda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
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

## Automation and Infrastructure

### Configuration Management

#### Podman Orchestration

  - **(2022)** [**redhat.com: How to automate Podman installation and deployment using Ansible 🌟**](https://www.redhat.com/en/blog/automate-podman-ansible) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Demonstrates the declarative configuration and automation of Podman host environments using Ansible modules. Covers setting up user namespaces for rootless execution, deploying container workloads, and auto-generating systemd services. High value for platform operations teams managing edge systems or bare-metal clusters.
## Container Technology

### Containerization

#### Best Practices

  - **(2021)** [thenewstack.io: Container Best Practices: What They Are and Why You Should Care](https://thenewstack.io/containers/container-best-practices-what-they-are-and-why-you-should-care) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines foundational container building guidelines, highlighting the use of minimal parent images (e.g., alpine, distroless), strict utilization of multi-stage builds, and running runtime processes as non-root users. These simple practices significantly mitigate security attack surfaces. This guide serves as a great starting point for development teams transitioning to containerized pipelines.
#### Security

  - **(2022)** [**How to use the --privileged flag with container engines**](https://www.redhat.com/en/blog/privileged-flag-container-engines) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An informative security overview regarding the risks of using the '--privileged' flag in container runtimes. Explains how this bypasses critical kernel isolation layers and presents alternative approaches, such as mapping selective Linux capabilities ('--cap-add') or rootless configurations to limit potential container breakouts.
### Daemonless Containerization

#### Automation

  - **(2021)** [redhat.com: Create fast, easy, and repeatable containers with Podman and shell scripts](https://www.redhat.com/en/blog/create-containers-podman-quickly) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide to wrapping Podman commands inside basic shell automation scripts to build repeatable and modular application runners. Emphasizes the lightweight nature of daemonless engines, showcasing that elaborate configurations can often be replaced by clean, low-dependency shell routines.
#### Compatibility Layers

  - **(2022)** [**redhat.com: Using Podman and Docker Compose**](https://www.redhat.com/en/blog/podman-docker-compose) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Walks through how to integrate Docker Compose configurations directly with Podman by leveraging Podman's API service socket. Offers a critical bridge for development teams with complex legacy Compose files who wish to transition to daemonless, rootless setups without rewriting their local deployment manifests.
  - **(2021)** [crunchtools.com: Should I Use Docker Compose Or Podman Compose With Podman?](http://crunchtools.com/should-i-use-docker-compose-or-podman-compose-with-podman) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates the differences between the Python-implemented Podman Compose utility and native Docker Compose coupled with Podman's backend API socket. Analyzes compatibility, performance, and volume-mounting differences to help engineers decide on the best strategy for local multi-container composition.
#### Edge and IoT

  - **(2021)** [==redhat.com: How to use auto-updates and rollbacks in Podman==](https://www.redhat.com/en/blog/podman-auto-updates-rollbacks) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Examines Podman's automated container update mechanics integrated with systemd. If an updated OCI container fails a health check on boot, Podman automatically rolls back the instance to the previous stable state. This unique, low-overhead pattern is critical for managing autonomous edge deployments and zero-touch remote operations.
#### Features Overview

  - **(2021)** [redhat.com: 5 Podman features to try now](https://www.redhat.com/en/blog/podman-features-1) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights five lesser-known Podman features, including local directory mounting without starting a container, native systemd service auto-generation, and structural image signing validation. This serves as an excellent reference for engineers looking to utilize the full capabilities of daemonless container engines.
#### Kubernetes Migration

  - **(2022)** [**redhat.com: From Docker Compose to Kubernetes with Podman**](https://www.redhat.com/en/blog/compose-kubernetes-podman) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Demonstrates Podman's capability to read and generate native Kubernetes YAML files using 'podman play kube' and 'podman generate kube'. This integration allows developers to design and test multi-container pods locally on their workstation before shipping the identical manifest to a Kubernetes production environment.
  - **(2022)** [**redhat.com: Build Kubernetes pods with Podman play kube**](https://www.redhat.com/en/blog/podman-play-kube-updates) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Discusses enhancements made to Podman's ability to ingest Kubernetes Pod, Deployment, and PersistentVolumeClaim YAML declarations. This capability allows developers to mock Kubernetes deployment scenarios locally using systemd-integrated Podman backends, accelerating local feedback cycles and lowering cloud resource costs.
#### MacOS Setup

  - **(2023)** [**redhat.com: How to replace Docker with Podman on a Mac, revisited**](https://www.redhat.com/en/blog/replace-docker-podman-mac-revisited) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Revisits macOS migrations to Podman, featuring optimizations to helper VMs, Rosetta 2 emulation for architecture transitions (x86/ARM), and enhanced volume sharing. These modifications simplify native Mac-based workflows, confirming Podman's status as a viable corporate tool for development teams.
  - **(2021)** [redhat.com: How to replace Docker with Podman on a Mac](https://www.redhat.com/en/blog/replace-docker-podman-macos) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step setup guide for configuring Podman on macOS platforms to replace proprietary desktop solutions. Details how to initiate the underlying Linux VM helper, map CLI aliases, and run basic rootless OCI images. Essential onboarding documentation for development teams migrating to open-source developer environments.
#### Observability

  - **(2021)** [redhat.com: How to use Podman to get information about your containers](https://www.redhat.com/en/blog/container-information-podman) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to use Podman diagnostic commands to inspect, log, and monitor containers. Focuses on filtering metadata arrays to verify port configurations, network bindings, and systemd hooks. Useful reference for systems administrators debugging rootless container deployments.
#### Podman

  - **(2026)** [==Libpod: Library and tool for running OCI-based containers in Pods==](https://github.com/containers/podman) <span class='md-tag md-tag--info'>⭐ 31763</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Libpod is the underlying library that hosts the Podman container management tool, enabling daemonless and rootless execution of OCI-compliant pods and containers. It brings Kubernetes pod primitives down to local workstations. In 2026, Podman remains the standard tool for local container manipulation on modern enterprise distributions.
#### Podman Ecosystem

  - **(2021)** [Podman remote clients for macOS and Windows](https://www.redhat.com/en/blog/podman-clients-macos-windows) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the architecture of remote Podman clients on macOS and Windows, which allow developers to manage containers running inside a localized Linux virtual machine. Leverages a secure REST API client configuration to bridge non-Linux developer hosts with backend container workloads without needing background system daemons.
#### Security (1)

  - **(2021)** [**redhat.com: Exploring the new Podman secret command 🌟**](https://www.redhat.com/en/blog/new-podman-secrets-command) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explores the Podman secrets API, enabling developers to declare and manage secrets locally without embedding sensitive values inside container layers or environment variables. Highlights Podman's architectural security posture by isolating secret storage within the user's home directory structures, aligning developer practices with production container security standards.
#### Systemd Integration

  - **(2023)** [==redhat.com/sysadmin/quadlet-podman==](https://www.redhat.com/en/blog/quadlet-podman) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A detailed analysis of Quadlet, a tool within the Podman ecosystem that simplifies running containers under systemd. Instead of writing verbose systemd files, Quadlet parses simple configuration declarations to automatically create native services. This pattern is the gold standard for managing rootless container lifecycles in production Linux systems.
### Image Management

#### Skopeo

  - **(2022)** [==Promoting container images between registries with skopeo==](https://www.redhat.com/en/blog/promoting-container-images-between-registries-with-skopeo) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A technical guide to utilizing Skopeo, a specialized utility designed for querying, copying, and signing container images directly across remote registries without needing local downloads or docker daemon engines. Skopeo is widely used in enterprise CI/CD pipelines to promote container images between registries with minimal latency and network overhead.
### Registries and Catalogs

#### Enterprise Repositories

  - **(2026)** [**Red Hat Ecosystem Catalog**](https://catalog.redhat.com/en/software/containers/explore) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The Red Hat Ecosystem Catalog provides vetted, secure, and optimized enterprise container images. This platform allows enterprise teams to secure their base image software supply chain by sourcing artifacts that undergo regular vulnerability scans and performance verification on Red Hat Enterprise Linux and OpenShift platforms.
### Runtimes

#### CRI-O and Podman Ecosystem

  - **(2022)** [**Why Red Hat is investing in CRI-O and Podman**](https://www.redhat.com/en/blog/why-red-hat-investing-cri-o-and-podman) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A strategic and technical explanation of Red Hat's investment in CRI-O as a Kubernetes-dedicated runtime, alongside Podman as a daemonless utility for local developer environments. Highlights the performance, stability, and security enhancements achieved by breaking away from the monolithic Docker daemon. This transition established the modern open-source container runtime standard.
#### Comparison and Architecture

  - **(2021)** [==inovex.de: Welcome To The Container Jungle: Docker vs. containerd vs. Nabla vs. Kata vs. Firecracker and more! 🌟==](https://www.inovex.de/de/blog/containers-docker-containerd-nabla-kata-firecracker) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A classic, comprehensive deep-dive comparing the design of traditional container runtimes (Docker, containerd) with microVM virtualization engines (Firecracker, Kata Containers) and sandboxed runtimes (Nabla). It evaluates trade-offs regarding startup speed, memory footprints, and multi-tenant security isolation. Highly referenced by platform architects as the definitive overview of runtime mechanics.
#### Legacy Adapters

  - **(2020)** [Frakti](https://github.com/kubernetes-retired/frakti) <span class='md-tag md-tag--info'>⭐ 675</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Critical Live Grounding: Frakti was built as a hypervisor-based Container Runtime Interface (CRI) for Kubernetes to execute runtimes like Kata Containers directly. This repository has been officially retired and archived by the Kubernetes organization. Contemporary architectures use direct runtime engine integrations via containerd and CRI-O, rendering Frakti legacy.
#### Performance Tuning

  - **(2022)** [**scrivano.org: the journey to speed up running OCI containers**](https://scrivano.org/posts/2022-10-21-the-journey-to-speed-up-oci-containers) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Chronicles the optimization journey taken to boost the instantiation speed of OCI-compliant containers. Focuses on file system overheads, image layer parsing, and low-level improvements inside container runtime layers. In 2026, these efforts are reflected in advanced image pulling techniques like eStargz and overlay-aware storage drivers.
### Standards

#### Open Container Initiative

  - **(2026)** [==OCI: Open Container Initiative==](https://opencontainers.org) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The home of the Open Container Initiative (OCI), standardizing industry specifications for container image layouts and runtime execution behaviors. This standard ensures interoperability and prevents vendor lock-in across the modern cloud-native landscape. In 2026, compliance with OCI specifications remains mandatory for every production-ready orchestrator and runtime.
## DevSecOps

### CICD Pipeline Security

#### Podman (1)

  - [Build trusted pipelines/Guards with Podman containers](https://www.redhat.com/en/blog/using-container-technology-make-trusted-pipeline)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Evaluates strategies for building rootless, secure continuous integration pipelines using Red Hat's Podman. Contrasts Podman's daemonless security with Docker's privileged execution models to prevent pipeline takeover attacks.
## Infrastructure

### Containerization (1)

#### Kernel Internals

  - [Controlling Process Resources with Linux Control Groups (cgroups)](https://labs.iximiuz.com/tutorials/controlling-process-resources-with-cgroups) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A deep, interactive laboratory walk-through demonstrating how Linux Control Groups (cgroups) throttle and isolate system resources. Crucial baseline knowledge for understanding container limits in Kubernetes.
## Observability (1)

### Logging

#### Command Line Tools

  - [bul: Interactive TUI for Exploring Kubernetes Container Logs](https://github.com/ynqa/bul) <span class='md-tag md-tag--info'>⭐ 16</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An interactive Terminal User Interface (TUI) written in Go for streaming and searching Kubernetes container logs. Grounding suggests that development has stalled (inactive for over 4 years), so while technically functional for local dev, tools like Stern or K9s are preferred in enterprise environments.

---
💡 **Explore Related:** [OCP 3](./ocp3.md) | [OCP 4](./ocp4.md) | [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md)

