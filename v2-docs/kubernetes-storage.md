# Kubernetes Storage. Cloud Native Storage

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-storage/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Storage. Cloud Native Storage in the context of The Container Stack.

## Cloud Native Storage Architecture

### Storage Architecture and Engines

#### Container Attached Storage

  - **(2020)** [thenewstack.io: Stateful Workloads on Kubernetes with Container Attached Storage 🌟](https://thenewstack.io/stateful-workloads-on-kubernetes-with-container-attached-storage) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exploration of Container Attached Storage (CAS) architectures, where storage software itself runs inside microservices to present local drives as resilient distributed storage pools. This approach, exemplified by OpenEBS and Portworx, maximizes hyper-converged agility.
#### Object Storage

  - **(2021)** [thenewstack.io: Beyond Block and File: COSI Enables Object Storage in Kubernetes 🌟](https://thenewstack.io/beyond-block-and-file-cosi-enables-object-storage-in-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural overview of the Container Object Storage Interface (COSI) initiative, which seeks to standardize object storage provisioning in Kubernetes, mirroring the success of CSI. COSI abstracts bucket creation and user management into a native Kubernetes API.
  - **(2021)** [infoworld.com: Kubernetes object storage best practices](https://www.infoworld.com/article/2269961/kubernetes-object-storage-best-practices.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An InfoWorld expert synthesis offering actionable guidelines on designing applications around object storage APIs instead of direct disk mounts. This approach enhances scaling metrics and simplifies geo-distributed cloud-native architectures.
#### Storage Paradigms

  - **(2020)** [blocksandfiles.com: geless storage is the ‘answer’ to Kubernetes data challenges](https://www.blocksandfiles.com/container-storage/2020/12/22/storageless-storage-is-the-answer-to-kubernetes-data-challenges/1611647) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exploratory piece discussing 'storageless' architecture paradigms where localized persistent state is completely abstract, delegating high availability and replica management to SaaS object systems. While conceptually novel, live implementation typically manifests as highly managed serverless databases.
### Storage Fundamentals

#### Stateful Applications

  - **(2021)** [developers.redhat.com: How to maximize data storage for microservices and Kubernetes, Part 1: An introduction 🌟](https://developers.redhat.com/articles/2021/08/11/how-maximize-data-storage-microservices-and-kubernetes-part-1-introduction) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of a premium Red Hat series defining technical best practices for mapping microservices to underlying storage topologies. It highlights the strategic balance between raw database performance demands and the cloud-native flexibility of dynamic storage provisioning.
  - **(2021)** [thenewstack.io: The Growth of State in Kubernetes](https://thenewstack.io/the-growth-of-state-in-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — A historical and architectural analysis of the growth of stateful applications inside Kubernetes. It documents the transition from early, experimental Peterson/Docker volume loops to highly hardened cloud-native database clustering engines.
  - **(2021)** [infoq.com: Best Practices for Running Stateful Applications on Kubernetes](https://www.infoq.com/articles/kubernetes-stateful-applications) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An InfoQ blueprint consolidating real-world best practices for operating large-scale stateful applications. It stresses the architectural value of strict volume lifecycle separation, graceful backup policies, and resilient node anti-affinity configuration rules.
  - **(2020)** [thenewstack.io: A Guide to Running Stateful Applications in Kubernetes](https://thenewstack.io/a-guide-to-running-stateful-applications-in-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A deep dive into the operational challenges and patterns involved in running stateful workloads on Kubernetes. It details how StatefulSets, headless services, and stable network identities collaborate to sustain clustered databases like PostgreSQL and Kafka safely.
#### Storage Paradigms (1)

  - **(2020)** [thenewstack.io: Compute and Storage Should Be Decoupled for Log Management at Scale](https://thenewstack.io/why-compute-and-storage-should-be-decoupled-for-log-management-at-scale) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural case study advocating for the strict decoupling of compute nodes and storage backends within log-aggregation systems. This pattern, exemplified by Loki and Elasticsearch, ensures that volatile search workloads do not degrade raw historical index durability.
## Kubernetes Storage Implementation

### Stateful Operations

#### Volume Resizing

  - **(2021)** [itnext.io: Resizing StatefulSet Persistent Volumes with zero downtime 🌟](https://itnext.io/resizing-statefulset-persistent-volumes-with-zero-downtime-916ebc65b1d4) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A highly valuable technical guide detailing how to resize StatefulSet Persistent Volumes with zero downtime. It details the complex mechanics of updating CSI drivers, triggering file system expansion, and safely editing stateful configurations online.
## Storage

### Kubernetes Storage

#### Distributed Block Storage

  - **(2026)** [==Longhorn==](https://longhorn.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Longhorn is a lightweight, distributed block storage system for Kubernetes, engineered as a graduated CNCF project. It abstracts hardware arrays by configuring a replica-aware storage engine for each volume, operating as dynamic microservices to deliver features like snapshots, automated backups, and cross-cluster replication.
  - **(2020)** [Longhorn Simplifies Distributed Block Storage in Kubernetes](https://www.suse.com/c/rancher_blog/longhorn-simplifies-distributed-block-storage-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical assessment highlighting how Longhorn simplifies the deployment and operations of distributed block storage arrays. It features detailed discussions of volume-controller microservice orchestration, automated disaster recovery policies, and built-in replication tools.
#### GlusterFS Orchestration

  - **(2026)** [==Kadalu==](https://github.com/kadalu/kadalu) <span class='md-tag md-tag--info'>⭐ 748</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f2c7d9d9" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 12 L 20 9 L 30 13 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-f2c7d9d9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kadalu is a lightweight, container-native storage solution that utilizes GlusterFS to orchestrate persistent volumes inside Kubernetes. It runs storage services inside application pods as microservices, offering a lightweight alternative to external GlusterFS cluster configurations.
## Storage and Data

### Container Attached Storage (1)

#### OpenEBS

  - **(2023)** [OpenEBS Features and Benefits](https://openebs.io/docs) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive guide to OpenEBS Container Attached Storage (CAS) engine. Details how local volumes, Jiva, and Mayastor architectures allow teams to build highly resilient, dynamic persistent storage volumes directly using local disk pools. CNCF validation confirms OpenEBS's position as a robust storage framework for stateful microservices.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

