# Kubernetes Backup and Migrations

!!! info "Architectural Context"
    Detailed reference for Kubernetes Backup and Migrations in the context of The Container Stack.

## Standard Reference

  - [medium: Velero backup/restore for K8s Stateful Applications managed by Operators](https://medium.com/@Sandeepkallazhi/velero-backup-restore-for-k8s-stateful-applications-managed-by-operators-8fd9c732ffcc?utm_sq=gi0vbpxxa3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [RKE2 Standalone Disaster Recovery Guide](https://support.tools/post/rke2-standalone-disaster-recovery)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Automate SQL Server Backups with PowerShell](https://datacrazyworld.com/index.php/2025/03/16/automatiza-backups-de-sql-server-con-powershell)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup) <span class='md-tag md-tag--info'>⭐ 493</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Stash](https://github.com/stashed/stash) <span class='md-tag md-tag--info'>⭐ 1414</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Cloud Native Backups, Disaster Recovery and Migrations on' Kubernetes](https://thenewstack.io/cloud-native-backups-disaster-recovery-and-migrations-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [k8s-snapshots: Automatic Volume Snapshots on Kubernetes](https://github.com/miracle2k/k8s-snapshots) <span class='md-tag md-tag--info'>⭐ 350</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [infracloud.io: Protecting Kubernetes applications data using Kanister](https://www.infracloud.io/blogs/protecting-kubernetes-applications-with-kanister)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: DevSecOps Teams Need Application-Consistent Backups for' Kubernetes Workloads](https://thenewstack.io/devsecops-teams-need-application-consistent-backups-for-kubernetes-workloads)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [longhorn issue: Move replica to a different server](https://github.com/longhorn/longhorn/issues/292) <span class='md-tag md-tag--info'>⭐ 7734</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [aithority.com: Bacula Systems Announces World’s First Enterprise-Class Backup' and Recovery Solution for Red Hat OpenShift](https://aithority.com/it-and-devops/cloud/bacula-systems-announces-worlds-first-enterprise-class-backup-and-recovery-solution-for-red-hat-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Red Hat Brings Backup, Snapshots to OpenShift Container' Storage](https://thenewstack.io/red-hat-brings-backup-snapshots-to-openshift-container-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: 5 Best Practices to Back up Kubernetes](https://thenewstack.io/5-best-practices-to-back-up-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Bacula Enterprise for OpenShift and Kubernetes 🌟](https://www.baculasystems.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dani-izquierdo95.medium.com: Batch processing using Cron Jobs. MySQL automated' backup on Openshift/K8s](https://dani-izquierdo95.medium.com/mysql-automated-backup-on-openshift-k8s-3690280d304f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Backup and Restore of Kubernetes Stateful Application Data with' CSI Volume Snapshots](https://itnext.io/backup-and-restore-of-kubernetes-stateful-application-data-with-csi-volume-snapshots-14ce9e6f3778)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Kubernetes Backup & Restore made easy! 🌟](https://dev.to/techworld_with_nana/kubernetes-backup-restore-made-easy-2nlg)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kasten.io: 10 Key Takeaways from Kubernetes Backup & Recovery For Dummies](https://blog.kasten.io/10-key-takeaways-from-kubernetes-backup-recovery-for-dummies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [k8up.io](https://k8up.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@amitabhprasad: Kubernetes volume backup for disaster recovery](https://medium.com/@amitabhprasad/kubernetes-volume-backup-for-disaster-recovery-56a5facee7fe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: K8s Backup and Disaster Recovery Is More Important Than' Ever](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [martinheinz.dev: Backup-and-Restore of Containers with Kubernetes Checkpointing' API](https://martinheinz.dev/blog/85)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Kubernetes.. ETCD Backup and Restore... Very Easy Steps... CKA' Exam Tips..](https://www.youtube.com/watch?app=desktop&v=mODkt1OJDew&ab_channel=AlokKumar)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/gardener/etcd-backup-restore](https://github.com/gardener/etcd-backup-restore) <span class='md-tag md-tag--info'>⭐ 328</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: Kubernetes 1.20: Kubernetes Volume Snapshot Moves to GA](https://kubernetes.io/blog/2020/12/10/kubernetes-1.20-volume-snapshot-moves-to-ga)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Leveraging operator pattern and VolumeSnapshots to backup databases' in Kubernetes](https://medium.com/blablacar/leveraging-operator-pattern-and-volumesnapshots-to-backup-databases-in-kubernetes-3a28aa425100)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [TrillioVault for Kubernetes](https://www.trilio.io/triliovault-for-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.kasten.io: Extending Kubernetes Application Backup and Mobility to' the Edge with Kasten K10 V4.5](https://blog.kasten.io/posts/extending-kubernetes-application-backup-and-mobility-to-the-edge-with-kasten-k10-v4.5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Kasten K10 V4.5: Grafana Observability, More Edge Support](https://thenewstack.io/kasten-k10-v4-5-grafana-observability-more-edge-support)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Kasten K10 on KubeSphere to Ensure Kubernetes Backup and Restore](https://faun.pub/kasten-k10-on-kubesphere-to-ensure-kubernetes-backup-and-restore-1bc59a0b91aa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [wecloudpro.com: Kubernetes Disaster Recovery with Velero 🌟](https://www.wecloudpro.com/2020/08/22/kubernetes-disaster-recovery-with-velero.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@firat.yasar: Backup & Restore Kubernetes resources with VELERO](https://medium.com/@firat.yasar/backup-restore-kubernetes-resources-with-velero-b7fee14e7664)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [skildops.medium.com: Backup an entire Kubernetes cluster using Velero to' AWS S3](https://skildops.medium.com/backup-an-entire-kubernetes-cluster-using-velero-to-aws-s3-73d76d51d4bc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: Backup, Restore and Migrate Kubernetes Cluster resources' using Velero](https://blog.devgenius.io/backup-restore-and-migrate-kubernetes-cluster-resources-using-velero-a9b6997e4b54)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [PX-Backup](https://portworx.com/products/px-backup)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/konveyor 🌟](https://github.com/konveyor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [engineering.konveyor.io: Konveyor Engineering Knowledgebase](https://engineering.konveyor.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Crane 2 Preview: Introduction and Demo](https://www.youtube.com/watch?v=esIZS7PVrvs&ab_channel=Konveyor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: Migrating Java JBoss EAP Applications to Kubernetes With' S2I](https://www.slideshare.net/KonveyorIO/migrating-java-jboss-eap-applications-to-kubernetes-with-s2i)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Application Migration

### Modernization

#### Enterprise Migration

  - **(2020)** [**konveyor 🌟**](https://konveyor.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — An open-source application modernization platform that helps developers migrate legacy virtual machines, stateful services, and bare-metal workloads to Kubernetes. It provides discovery, analysis, and execution tools for large-scale container migrations.
## Cloud Providers

### Google Cloud Platform

#### Data Protection

  - [cloud.google.com: Announcing Backup for GKE: the easiest way to protect' GKE workloads](https://cloud.google.com/blog/products/storage-data-transfer/google-cloud-launches-backups-for-gke) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep dive into the native GKE Backup service, designed for stateful application restoration and cluster disaster recovery. Discusses how to safeguard configuration metadata and persistent volume states natively through GCP APIs.
## Orchestration

### Kubernetes Migration

#### Konveyor Tooling

  - **(2025)** [==github.com/konveyor/crane: Crane 2.0 🌟==](https://github.com/migtools/crane) <span class='md-tag md-tag--info'>⭐ 54</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Part of the Konveyor ecosystem, Crane enables seamless state transfer and application migration between Kubernetes clusters. Facilitates dry-runs, resource translation, and continuous PV synchronization during heavy environment-replatforming processes.
  - **(2022)** [kubebyexample.com: Migrating to Kubernetes with Open Source Tools (Konveyor, Tackle, KubeVirt, Forklift) 🌟](https://kubebyexample.com/community/blog/migrating-to-kubernetes-with-open-source-tools) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Describes migrations using open-source platforms like Tackle, Crane, KubeVirt, and Forklift. Provides platform architects with a reference strategy to migrate legacy virtual machines directly into containers on Kubernetes.
  - **(2021)** [containerjournal.com: Red Hat, IBM Launch Konveyor to Aggregate Kubernetes Tools](https://cloudnativenow.com/features/red-hat-ibm-launch-konveyor-to-aggregate-kubernetes-tools) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reports the creation and open-sourcing of Konveyor, a unified suite of migration tools launched by Red Hat and IBM. Facilitates the assessment and modernization of virtualization and container workloads to standard Kubernetes infrastructure.
### Kubernetes Operations

#### Data Protection (1)

  - **(2026)** [Trillio](http://trilio.io) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — TrilioVault for Kubernetes is a cloud-native, application-centric data protection platform. Offers automated backup, restore, migration, and disaster recovery capabilities native to the Kubernetes API, supporting Helm, Operators, and GitOps workflows.
  - **(2026)** [Kasten](https://www.veeam.com/products/cloud/kubernetes-data-protection.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kasten K10 by Veeam stands as an industry-standard data management and disaster recovery platform built for Kubernetes. Features automatic discovery, policy-based backup, end-to-end security compliance, and recovery orchestration across heterogeneous cloud systems.
#### Disaster Recovery

  - **(2022)** [rancher.com: The No. 1 Rule of Disaster Recovery](https://www.suse.com/c/rancher_blog/the-no-1-rule-of-disaster-recovery) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details crucial disaster recovery paradigms within cloud-native and Kubernetes orchestrations. Focuses on the 'test your restore' rule, highlighting that a backup is only as reliable as its validation testing. Explores automated recovery validation techniques.
  - **(2022)** [rancher.com: Disaster Recovery Preparedness for Your Kubernetes Clusters 🌟](https://www.suse.com/c/rancher_blog/disaster-recovery-preparedness-for-your-kubernetes-clusters) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines a strategic readiness model for multi-cluster disaster recovery in Kubernetes. Evaluates backup schedules for etcd, cluster state synchronization, persistent volume replication, and declarative configuration preservation across failure domains.
#### Enterprise Backup

  - **(2024)** [PX-Backup: docs](https://docs.portworx.com/portworx-backup-on-prem) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documentation for Portworx PX-Backup, an enterprise solution specializing in application-consistent multi-cloud Kubernetes backups. Manages namespace-level state, metadata, and PV backing volumes with instant recovery options across production systems.
#### Velero Backup

  - **(2026)** [==github.com/vmware-tanzu/velero==](https://github.com/velero-io/velero) <span class='md-tag md-tag--info'>⭐ 10028</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Velero is the prominent open-source utility for safely backing up, restoring, and migrating Kubernetes cluster resources and persistent volumes. Integrates closely with cloud provider storage APIs or generic file-level backups via Kopia or Restic.
  - **(2023)** [akomljen.com: Kubernetes Backup and Restore with Velero 🌟](https://akomljen.com/kubernetes-backup-and-restore-with-velero/?utm_sq=ggwzo8xdd8) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive setup guide explaining Velero's deployment architecture and operational usage. Guides readers through backing up cluster state to S3-compatible endpoints, managing schedules, and restoring critical applications across namespace boundaries.
  - **(2023)** [cloud.redhat.com: Velero Backup and Restore of an Application Using gp2 StorageClass on ROSA](https://www.redhat.com/en/blog/velero-backup-and-restore-of-an-application-using-gp2-storageclass-on-rosa) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates enterprise deployment of Velero on Red Hat OpenShift on AWS (ROSA). Focuses on orchestrating persistent volume backups utilizing the AWS EBS CSI driver and migrating storage assets without workflow disruption.
### Kubernetes Storage

#### Enterprise Backup (1)

  - **(2021)** [blocksandfiles.com: Red Hat OpenShift now does container storage backup 🌟](https://www.blocksandfiles.com/container-storage/2021/01/27/red-hat-openshift-now-does-container-storage-backup/1611166) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reports on the introduction of native application and storage data-protection capabilities within Red Hat OpenShift. Discusses integrated control planes for disaster recovery, multi-cloud replication, and stateful volume backup management.
#### Snapshots

  - **(2024)** [blog.palark.com: Kubernetes snapshots: What are they and how to use them? 🌟](https://palark.com/blog/kubernetes-snaphots-usage) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the Kubernetes Container Storage Interface (CSI) Snapshot mechanism. Deeply explains the interaction between VolumeSnapshotClass, VolumeSnapshot, and VolumeSnapshotContent resources, enabling storage-agnostic point-in-time recovery.
  - **(2023)** [percona.com: Using Volume Snapshot/Clone in Kubernetes (GKE & Percona Kubernetes Operator for XtraDB Cluster)](https://www.percona.com/blog/using-volume-snapshot-clone-in-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical implementation guide for using CSI Volume Snapshots and Volume Clones under Kubernetes. Showcases application state restoration scenarios using the Percona Kubernetes Operator for XtraDB Cluster, proving stateful application resilience.

---
💡 **Explore Related:** [OCP 3](./ocp3.md) | [OCP 4](./ocp4.md) | [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md)

