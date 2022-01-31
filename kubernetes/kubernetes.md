---

title: ''
author: Cody Buell
date: 2022-01-24
extensions:
  - terminal
  - grapheasy
  - file_loader
  - tai
styles:
  style: tomorrownight
  margin:
    left: 2
    right: 2
    top: 0
    bottom: 1
  padding:
    left: 2
    right: 2
    top: 1
    bottom: 1
  author:
    fg: '#aaa,bold'
  slides:
    fg: '#aaa,bold'
  title:
    fg: '#aaa,bold'
  link:
    fg: '#cc6666,underline'
  headings:
    '1':
      fg: '#cc6666,bold'
      prefix: '████ '
    '2':
      fg: '#de935f,bold'
      prefix: '▓▓▓ '
    '3':
      fg: '#f0c674,bold'
      prefix: '▒▒ '
    '4':
      fg: '#81a2be,bold'
      prefix: '░ '

---

| Introduction to Kubernetes             |
|:--------------------------------------:|
|MMMMMMMMMMMMMMMWN0xddx0NWMMMMMMMMMMMMMMM|
|MMMMMMMMMMMWNKOxoc....coxOKNWMMMMMMMMMMM|
|MMMMMMMWNKOxoc....cccc....coxOKNWMMMMMMM|
|MMMWN0kdlc........dOOd........cldk0NWMMM|
|MMW0oc...........cxKKxc...........co0WMM|
|MMXd...cdoc..lxO0KNWWNK0Odl..codc...dXMM|
|MWOl...cxOOk0XK0kxKWWKxk0XXOkOOxc...l0WM|
|MNx......l0WWNOo.cOWWOc.oONWW0l......xNM|
|W0l.....cxNXk0XX0OXMMXO0XXOkXNxc.....l0W|
|Nx......lKNx.cdKWWX00XWWKdc.xNKl......xN|
|0l......oXNOkO0NWNO..ONWN0Ok0NXo......lK|
|xc..cokkOXWNKOkkKWWNNWWKkkOKNWXOkkdc..cx|
|d...cldoldXNkc.oKWKkkKWKo.ckNXdlodl....x|
|Xxc.......o0N0k0N0l..l0N0k0N0o.......cxX|
|MW0o.......cd0NWWKkkkkKWWN0dc.......o0WM|
|MMWXkl......cxKOkkOOOOkkOKxc......lkXMMM|
|MMMMWKdc....oOxc........cxOo....cdKWMMMM|
|MMMMMMNOl...ccc..........ccc...lONWMMMMM|
|MMMMMMMWXxc..................cxXWMMMMMMM|
|MMMMMMMMMNOdoooooooooooooooodONMMMMMMMMM|
|MMMMMMMMMMMMMMMWN0xddx0NWMMMMMMMMMMMMMMM|


- Introduction
- Goal
  - Basic understanding of what Kubernetes is.
  - Provide a starting point to build on.
- Hardest part is getting started, this will hopefully simplify that process a
  bit with a basic framework of understanding.

---

# Overview
 
```grapheasy
[the problem] -> [a solution] -> [componenets] -> [getting started]
```

> I barely understand my own feelings how am I supposed to understand
> kubernetes
>
> -- _[@iamdeveloper][1]_


- 🤨 This stuff is complex!


- 🙋 Please ask if you have questions.


- 🖱️  LET'S DOUBLE-CLICK ON THIS FYSA!

[1]: https://twitter.com/iamdevloper/status/1408773099059830784?lang=en

---

# First, What is Kubernetes?

> Kubernetes is a portable, extensible, open-source platform for managing
> containerized workloads and services, that facilitates both declarative
> configuration and automation. It has a large, rapidly growing ecosystem.
> Kubernetes services, support, and tools are widely available.
>
> -- _[kubernetes.io][2]_

__Short version:__ Kubernetes is a container orchestration tool.

To better understand what problem Kubernetes tries to solve we need a bit of
background on application architectures and the move to 'microservices'.

[2]: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/

---

# Traditional Application Deployments

|                                                             |
|:-----------------------------------------------------------:|
| ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ |
| │       │ │       │ │       │ │       │ │       │ │       │ |
| │       │ │       │ │       │ │       │ │       │ │       │ |
| │  APP  │ │  APP  │ │  APP  │ │  APP  │ │  APP  │ │  APP  │ |
| │       │ │       │ │       │ │       │ │       │ │       │ |
| │       │ │       │ │       │ │       │ │       │ │       │ |
| └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                                                         │ |
| │                     OPERATING SYSTEM                    │ |
| │                                                         │ |
| └─────────────────────────────────────────────────────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                                                         │ |
| │                         HARDWARE                        │ |
| │                                                         │ |
| └─────────────────────────────────────────────────────────┘ |
|                                                             |

Bottom up: 
  - __Hardware__ is your processor, memory, storage, etc.
  - __Operating System__ runs on that and sends instructions the underlying
    resources and makes them available to the applications which sit at the
    top.

Your laptop / personal computer is a good example of this model.

The challenge here is that there is a lot to consider:
  - __Variability__ of underlying hardware and operating system configurations
  - Apps competing for resources, __conflicting requirements__
  - __Underutilization__ of available hardware resources, or difficult to fully utilize resources

---

# Virtualised Application Deployments

|                                                             |
|:-----------------------------------------------------------:|
| ┌───────────────────────────┐ ┌───────────────────────────┐ |
| │  ┌─────┐ ┌─────┐ ┌─────┐  │ │  ┌─────┐ ┌─────┐ ┌─────┐  │ |
| │  │ APP │ │ APP │ │ APP │  │ │  │ APP │ │ APP │ │ APP │  │ |
| │  └─────┘ └─────┘ └─────┘  │ │  └─────┘ └─────┘ └─────┘  │ |
| │  ┌─────────────────────┐  │ │  ┌─────────────────────┐  │ |
| │  │   OPERATING SYSTEM  │  │ │  │   OPERATING SYSTEM  │  │ |
| │  └─────────────────────┘  │ │  └─────────────────────┘  │ |
| └───────────────────────────┘ └───────────────────────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                       HYPERVISOR                        │ |
| └─────────────────────────────────────────────────────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                     OPERATING SYSTEM                    │ |
| └─────────────────────────────────────────────────────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                         HARDWARE                        │ |
| └─────────────────────────────────────────────────────────┘ |
|                                                             |

Eventually virtual machines came along, they are nice in that you can build one
specifically for your needs and assign it some set of resources. You could
isolate application by common needs such as OS configuration etc.

- Hardware layer and OS stay the same.
- How have a hypervisor which __simulates hardware__ allowing you to install an
  operating system on top of it.

The problem here is that __it is a heavy configuration__:
- There is a lot of work involved in setup.
- You now have a hypervisor sitting directly on top of the OS, though type 1
  hypervisors exist which ride on bare metal, but still you have to manage it.
- You also have to deal with another full operating system level within your VM's.
- Patching, configuring, etc. Quite laborious to build, provision, and maintain.

---

# Containerized Application Deployments

|                                                             |
|:-----------------------------------------------------------:|
| ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ |
| │         │ │         │ │         │ │         │ │         │ |
| │ ┌─────┐ │ │ ┌─────┐ │ │ ┌─────┐ │ │ ┌─────┐ │ │ ┌─────┐ │ |
| │ │ APP │ │ │ │ APP │ │ │ │ APP │ │ │ │ APP │ │ │ │ APP │ │ |
| │ └─────┘ │ │ └─────┘ │ │ └─────┘ │ │ └─────┘ │ │ └─────┘ │ |
| │ bin/lib │ │ bin/lib │ │ bin/lib │ │ bin/lib │ │ bin/lib │ |
| │         │ │         │ │         │ │         │ │         │ |
| └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                    CONTAINER RUNTIME                    │ |
| └─────────────────────────────────────────────────────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                     OPERATING SYSTEM                    │ |
| └─────────────────────────────────────────────────────────┘ |
| ┌─────────────────────────────────────────────────────────┐ |
| │                         HARDWARE                        │ |
| └─────────────────────────────────────────────────────────┘ |
|                                                             |

- Container runtime instead of hypervisor which instead of simulating hardware
  simulates an underlying operating system.

Because of the relatively high effort lift to provision and configure vm's you
generally just make as few as possible to get the job done.

With containers however things change significantly. They are light and quick
to provision. Where running one VM would represent a significant resource load,
several containers are negligible. Lower barrier to entry, easier to isolate
workloads, or even components of workloads.

- Tightly controlled minimalist environments, much easier to have consistency
- Like a chrooted (own filesystem) and cgrouped (own cpu and mem) environment, able to utilize parent os
- Very light weight, so quick to provision, restart etc
- You create a container at release rather than at deployment in sdlc
- Runs the same regardless of underlying host, agnostic and portable across providers, avoids tie in
- So light weight that it is not a concern to make a container for each component of your app

- But you have to maintain containers, if one goes down you have to turn it back on, providing resources, etc.

---

# The Problem

- It requires a lot of work to manage containers directly.
  - Networking them together (and between hosts)
  - Persistence of data
  - Scaling with demand
  - Disaster recovery
  - ...
- Too much too manage manually in production

# Kubernetes' Solution

- Kubernetes abstracts out the underlying bits and provides a single
  environment to run and manage containerized applications.
- Kubernetes provides:
  - High Availability
  - Scalability
  - Disaster Recovery
- Kubernetes does not provide:
  - Host configuration management
  - Persistent storage
  - A Container runtime

---

# Hardware Layer

|                                                                         |
|:-----------------------------------------------------------------------:|
| ┌─────────────────────────────────────────────────────────────────────┐ |
| │                                                                     │ |
| │                         Kubernetes Cluster                          │ |
| │                                                                     │ |
| └─────────────────────────────────────────────────────────────────────┘ |
| ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐ |
| │                     │ │                     │ │                     │ |
| │                     │ │                     │ │                     │ |
| │    Control Plane    │ │     Worker Node     │ │     Worker Node     │ |
| │                     │ │                     │ │                     │ |
| │                     │ │                     │ │                     │ |
| └─────────────────────┘ └─────────────────────┘ └─────────────────────┘ |
| ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐ |
| │   OPERATING SYSTEM  │ │   OPERATING SYSTEM  │ │   OPERATING SYSTEM  │ |
| └─────────────────────┘ └─────────────────────┘ └─────────────────────┘ |
| ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐ |
| │       HARDWARE      │ │       HARDWARE      │ │       HARDWARE      │ |
| └─────────────────────┘ └─────────────────────┘ └─────────────────────┘ |
|                                                                         |

- Nodes
  - Control Plane / Master / Server
  - Worker / Agent

---

# Software Layer

|                                                                         |
|:-----------------------------------------------------------------------:|
| ┌─────────────────────────────────────────────────────────────────────┐ |
| │                                                                     │ |
| │                         Kubernetes Cluster                          │ |
| │                                                                     │ |
| └─────────────────────────────────────────────────────────────────────┘ |
| ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐ |
| │ Control Plane       │ │ Worker Node         │ │     Worker Node     │ |
| │  - api server       │ │  - kubelet          │ │         ...         │ |
| │  - controller mngr  │ │  - kube-proxy       │ │                     │ |
| │  - scheduler        │ │  - container rntm   │ │                     │ |
| │  - etcd             │ │                     │ │                     │ |
| └─────────────────────┘ └─────────────────────┘ └─────────────────────┘ |
| ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐ |
| │   OPERATING SYSTEM  │ │   OPERATING SYSTEM  │ │   OPERATING SYSTEM  │ |
| └─────────────────────┘ └─────────────────────┘ └─────────────────────┘ |
| ┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐ |
| │       HARDWARE      │ │       HARDWARE      │ │       HARDWARE      │ |
| └─────────────────────┘ └─────────────────────┘ └─────────────────────┘ |
|                                                                         |

- Nodes
  - Control Plane / Master / Server
    - __api server:__ a container running api frontend, interfaces with kubectl
    - __contorller manager:__ handles cluster status and configuration
    - __scheduler:__ manages container coordination among worker / agent nodes
    - __etcd:__ a key value store that holds the state of the cluster
    - __virtual network__: the isolated kubernetes cluster environment
  - Worker / Agent
    - __kubelet:__ an agent that monitors and runs the containers
    - __kube-proxy__: handles the cluster networking for the node
    - __container runtime:__ what actually runs the containers

---

# Cluster Components

|                                                                         |
|:-----------------------------------------------------------------------:|
| ┌─────────────────────────────────────────────────────┬─────────────┬─┐ |
| │                         Kubernetes Cluster          ├─────────────┤ │ |
| │                                                     │             │ │ |
| │   ┌───────────┐                                     │  Node Port  │ │ |
| │   │    Pod    │                                     │             │ │ |
| │   │           │                                     └──────┬──────┘ │ |
| │   │ container │◄─────┐                                     │        │ |
| │   │ container │      │       ┌───────────────┐             │        │ |
| │   └───────────┘      └───────┤               │◄────────────┘        │ |
| │                              │    Service    │                      │ |
| │   ┌───────────┐      ┌───────┤               │◄────────────┐        │ |
| │   │    Pod    │      │       └───────────────┘             │        │ |
| │   │           │◄─────┘                              ┌──────┴──────┐ │ |
| │   │ container │                                     │             │ │ |
| │   │ container │                                     │   Ingress   │ │ |
| │   └───────────┘                                     │             │ │ |
| │                                                     ├─────────────┤ │ |
| └─────────────────────────────────────────────────────┴─────────────┴─┘ |
|                                                                         |

- __Pods:__ 
  - An abstraction of containers.
  - Ephemeral, always moving around hosts, changing ip's, etc
  - Composed of one or more containers constituting a logical workload.
  - One pod per application / microservice
  - Containers in a pod should be tightly coupled:
    - They share an ip and disk
    - Close analogy is they are apps installed on same machine
    - Logging utility / service, Prometheus client, etc
- __Services:__
  - Sit in front of pods, not tied to their life-cycle.
  - Pods will come and go but services stay and provide a way to find the pods.
  - Provide two things:
    - __Static IP__ allowing us to define configs tying things together.
    - __Load Balancing__ by forwarding specified ports to the target pods.
  - Two general types:
    - Internal
      - __ClusterIP:__ The default. Id's pods by tags, load balances configured ports.
      - __Headless:__ A ClusterIP that has ClusterIP set to None, special case for stateful apps.
    - External
      - __Node Port:__ An extension of ClusterIP. Makes a port accessible on
        all worker nodes. `30,000 -> 32,767`. Routes `host port -> service port -> pod port`.
      - __Load Balancer:__ An extension of Node Port which also provisions a
        csp provided load balancer between the worker nodes.
- Ingress:
  - An externally exposed service that sits on privileged ports (80, 443) and routes traffic in to other services.
  - Can route based on the incoming request:
    - __host__, eg mysite.com vs yoursite.com
    - __path__, eg /about vs /products

---

# Other Common Components

- __ConfigMaps__ Make environment variables and properties files available to pods.


- __Secrets__ Like ConfigMaps but base64 encoded... 🤷


- __Volumes__ Provide persistent storage to pods.


- __Deployment__
  - For stateless applications
  - Defines a desired state for you pods, eg "I want 2 replicas of this pod which runs these containers".
  - Used instead of defining pods directly.


- __Stateful Set__
  - Like a Deployment but for stateful applications.
  - Complex... A way of shimming things that won't run well in Kubernetes into Kubernetes

---

# Manifests

Manifests are how we tell Kubernetes what to do.

```file
path: ./code/pod-manifest.yml
lang: yaml
```

---

# Questions?
```tai24
./gifs/confused.gif -s 1
```

---

# Getting Started

- minikube

# Practical Personal / Home Uses

- PiHole
- Bitwarden
- Homebridge
- Media server
- UniFi Controller
- Dynamic DNS client
- Minecraft / game server
- OpenFaaS (at home lambda)
- Local development / testing
- ...

---

# Resources

### Learning

- [Kubernetes Overview Docs](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
- [TechWorld with Nana](https://www.youtube.com/c/TechWorldwithNana)

### Tools

- [K3S](https://k3s.io/) Single binary light weight Kubernetes installations!
- [Helm](https://helm.sh/) Templating for Kubernetes manifisets.
- [minikube](https://minikube.sigs.k8s.io/docs/) Local Kubernetes installation. `<-- START HERE`
- [Lens](https://k8slens.dev/) Advanced dashboarding for Kubernetes environments.
- [kOps](https://kops.sigs.k8s.io/) Tooling for cluster provisioning.
