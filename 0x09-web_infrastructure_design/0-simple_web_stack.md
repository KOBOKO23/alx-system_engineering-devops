<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Simple web stack</h1>
    <img src="https://github.com/KOBOKO23/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png" alt="Simple web stack">
    <h2>Description</h2>
    <p>This is a simple web infrastructure that hosts a website that is reachable via www.foobar.com. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.</p>
    <h3>Specifics About This Infrastructure</h3>
    <ul>
      <li>What a server is.</li>
      <p>A server is a computer hardware or software that provides services to other computers, which are usually referred to as clients.</p>
      <li>The role of the domain name.</li>
      <p>To provide a human-friendly alias for an IP Address. For example, the domain name www.wikipedia.org is easier to recognize and remember than 91.198.174.192. The IP address and domain name alias is mapped in the Domain Name System (DNS)</p>
      <li>The type of DNS record <em>www</em> is in <em>www.foobar.com.</em></li>
      <p>www.foobar.com uses an A record. This can be checked by running dig www.foobar.com.
<strong>Note:</strong> the results might be different but for the infrastructure in this design, an A record is used.
<i>Address Mapping record (A Record)—also known as a DNS host record, stores a hostname and its corresponding IPv4 address.</i></p>
      <li>The role of the web server.</li>
      <p>The web server is a software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.</p>
      <li>The role of the application server.</li>
      <p>To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications.</p>
      <li>The role of the database.</li>
      <p>To maintain a collection of organized information that can easily be accessed, managed and updated.</p>
      <p>What the server uses to communicate with the client (computer of the user requesting the website).
	Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.</p>
      </ul>

    <h4>Issues With This Infrastructure</h4>

    <ul>
      <li>There are multiple SPOF (Single Point Of Failure) in this infrastructure.</li>
	<p>For example, if the MySQL database server is down, the entire site would be down.</p>
      <li>Downtime when maintenance needed.</li>
      <p>When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.</p>
      <li>Cannot scale if there's too much incoming traffic.</li>
      <p>It would be hard to scale this infrastructure becauses one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of requests.</p>
      
</body>
</html>
