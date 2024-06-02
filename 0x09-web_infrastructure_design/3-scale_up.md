<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Scaled Up Web Infrastructure</h1>
    <img src="https://github.com/KOBOKO23/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.png" alt="Scaled Up Web Infrastructure">
    <h2>Description</h2>
    <p>This web infrastructure is a scaled up version of the infrastructure described here. In this version, all SPOFs have been removed and each of the major components (web server, application server, and database servers) have been moved to separate GNU/Linux servers. The SSL protection isn't terminated at the load-balancer and each server's network is protected with a firewall and they're also monitored.</p>
    <h3>Specifics About This Infrastructure</h3>
    <ul>
      <li>The addition of a firewall between each server.<li>
      <p>This protects each server from unwanted and unauthorized users rather than protecting a single server.</p>
    </ul>
    
    <h4>Issues With This Infrastructure</h4>

    <ul>
      <li>High maintenance costs.<li>
      <p>Moving each of the major components to its own server, means that more servers would have to be bought and the company's electricity bill would rise along with the introduction of new servers. Some of the company's funds would have to be used to buy the servers and pay for the electricity consumption needed to keep the servers (including the new and old ones) running.</p>
      </ul>
      
</body>
</html>
