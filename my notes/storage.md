storage understanding:
- What is data storage?
	- Data storage is the collection and retention of digital information—the bits and bytes behind applications, network protocols, documents, media, address books, user preferences, and more.

- Different type of storage:
	- software-defined storage:
		- Software-defined storage (SDS) is a storage architecture that separates storage software from its hardware. Unlike traditional network-attached storage (NAS) or storage area network (SAN) systems, SDS is generally designed to perform on any industry-standard or x86 system, removing the software’s dependence on proprietary hardware.
		- Decoupling storage software from its hardware allows you to expand your storage capacity as you see fit, when you see fit, instead of scrambling to add another piece of proprietary hardware. It also allows you to upgrade or downgrade hardware whenever you want. Basically, SDS puts enormous flexibility in your hands.
		- Here’s the gist. Let’s say you have a bunch of different x86 servers. Each has a different storage capacity, and each needs a different kind of storage software to work. SDS allows you to remove the storage capacity on these inflexible pieces of hardware and put it all in a place that’s infinitely flexible—and scalable. With SDS, you can grow your storage capacity nearly instantly, making it cost effective as well as flexible and scalable. But that doesn’t make SDS a cloud (more on that later).
		- SDS is part of a larger ecosystem called hyperconverged infrastructure (loosely defined as software-defined everything) where all software is separated from all hardware. That division grants you the freedom to choose which hardware you purchase and how much storage you really need.
		- Old-school, traditional storage is monolithic. It’s sold as a bundle of hardware (often industry standard) and proprietary software. But the usefulness of SDS lies in its independence from any specific hardware.
		- In most cases, SDS should have:
			- Automation: Simplified management that keeps costs down.
			- Standard interfaces: An application programming interface (API) for management and maintenance of storage devices and services.
			- A virtualized data path: Block, file, and object interfaces that support applications written to these interfaces.
			- Scalability: The ability to scale out storage infrastructure without impeding performance.
			- Transparency: The ability to monitor and manage storage use while knowing what resources are available and at what costs.
		- How software-defined storage works
			- Software-defined storage is an approach to data management in which data storage resources are abstracted from the underlying physical storage hardware and are therefore more flexible. Resource flexibility is paired with programmability to enable storage that rapidly and automatically adapts to new demands. This programmability includes policy-based management of resources and automated provisioning and reassignment of the storage capacity.
		- Types of software-defined storage
		 	- A range of software-defined storage types exist in the market today, including:
				- Hypervisor-based
    			- Container-based (for example, running in a Docker container)
    			- Scale-out storage for unstructured data
    			- Distributed file systems for object storage offload
    			- HCI software (storage is combined with networking, compute, and virtualization software in the same package)


    - cloud storage:
    	- Cloud storage is the abstraction, pooling, and sharing of storage resources through the internet. Cloud storage is facilitated by IT environments known as clouds, which enable cloud computing—the act of running workloads within a cloud environment. 
    	- There are 3 types of cloud storage: public cloud storage, private cloud storage, and hybrid cloud storage. There are also 3 ways to format this storage: As blocks, files, or objects. Each format has its pros and cons (blocks are faster, files are easier to understand, and objects work best with quick moving workloads), but some software-defined cloud storage products can combine all 3 formats into a unified, easy-to-deploy solution.
    	- Many organizations are discovering that traditional storage methods can be the bottleneck that slows their agility and scalability. This has led to the development of containers, which allow applications to scale rapidly, be more reliable, and offer better performance than more conventional means or methods.
    	- Cloud storage formats:
			- Block Storage
				- Block storage splits a single storage volume (like a cloud storage node) into individual instances known as blocks. It's a fast, low latency storage system ideal for high performance workloads.
			- Object Storage 
				- Object storage involves pairing a piece of data with unique identifiers known as metadata. Since objects are uncompressed and unencrypted, they can be accessed very quickly at huge scale—making them ideal for cloud-native applications.
			- File storage
				- File storage is the dominant technology used on NAS systems and is responsible for organizing data and representing it to users. Its hierarchical structure allows us to navigate data from top to bottom easily, but increases processing time.
		- What is block storage?
			- Block storage chops data into blocks—get it?—and stores them as separate pieces. Each block of data is given a unique identifier, which allows a storage system to place the smaller pieces of data wherever is most convenient. 
			- Block storage is often configured to decouple the data from the user’s environment and spread it across multiple environments that can better serve the data. And then, when data is requested, the underlying storage software reassembles the blocks of data from these environments and presents them back to the user. It is usually deployed in storage-area network (SAN) environments and must be tied to a functioning server.
			- Because block storage doesn’t rely on a single path to data—like file storage does—it can be retrieved quickly. Each block lives on its own and can be partitioned so it can be accessed in a different operating system, which gives the user complete freedom to configure their data. It’s an efficient and reliable way to store data and is easy to use and manage.


















