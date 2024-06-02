<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Distributed Web Infrastructure</h1>
    <img src="https://github.com/KOBOKO23/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png" alt="Distributed Web Infrastructure">
    <h2>Description</h2>
    <pThis is a distributed web infrastructure that atttempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).</p>
    <h3>Specifics About This Infrastructure</h3>
    <ul>
      <li>The distribution algorithm the load balancer is configured with and how it works.</li>
      <p>The HAProxy load balancer is configured with the Round Robin distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.</p>
      <li>The setup enabled by the load-balancer.</li>
      <p>The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an Active-Passive setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.</li>
      <li>How a database Primary-Replica (Master-Slave) cluster works.</li>
      <p>A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.</p>
      <li>The difference between the Primary node and the Replica node in regard to the application.</li>
      <p>The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.</p>
      </ul>

    <h4>Issues With This Infrastructure</h4>

    <ul>
      <li>There are multiple SPOF (Single Point Of Failure) in this infrastructure.</li>
	<p>For example, if the MySQL database server is down, the entire site would be down.</p>
      <li>Security issues.</li>
      <p>The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.</p>
      <li>No monitoring.</li>
      <p>We have no way of knowing the status of each server since they're not being monitored.</p>
      
</body>
</html>
