### Incident Report: API Service Outage

**Issue Summary:**
On August 20, 2024, from 14:00 to 15:45 UTC, our primary API service experienced an outage that lasted 1 hour and 45 minutes. During this period, 80% of users were unable to access the service, while the remaining 20% experienced significant latency, with response times exceeding 10 seconds. The root cause of the issue was a misconfigured load balancer that caused a bottleneck, preventing the API requests from being routed properly to backend servers.

### Timeline:

- **14:05 UTC**: Issue detected via a monitoring alert indicating a sharp drop in API response success rates.
- **14:10 UTC**: Initial investigation began focusing on the API service itself; the API servers were checked for high memory or CPU usage.
- **14:20 UTC**: Further alerts received, pointing to increased error rates and timeouts across various endpoints.
- **14:25 UTC**: Assumptions were made that the issue was related to a recent API update; rollback procedures were initiated.
- **14:30 UTC**: Rollback completed, but the issue persisted. The focus shifted to the database, suspecting connection pool exhaustion.
- **14:40 UTC**: Database logs reviewed, no anomalies found. Misleading path led to an investigation of network firewalls, which also showed no issues.
- **14:50 UTC**: The incident was escalated to the networking team for further investigation.
- **15:00 UTC**: Networking team identified abnormal traffic patterns to the load balancer, which prompted a configuration review.
- **15:20 UTC**: Misconfiguration in the load balancer was found; traffic was being routed to a single backend server instead of the entire pool.
- **15:30 UTC**: Load balancer configuration was corrected to distribute traffic evenly.
- **15:40 UTC**: Monitoring confirmed that API response times were returning to normal levels.
- **15:45 UTC**: Incident resolved, and all systems confirmed to be fully operational.

### Root Cause and Resolution:

The root cause of the outage was a misconfiguration in the load balancer that routed all API traffic to a single backend server, overwhelming it and causing a bottleneck. The issue was introduced during a routine maintenance update to the load balancer configuration, where the server pool setting was inadvertently altered. As a result, the other servers in the pool received no traffic, and the single overloaded server caused the API service to fail for the majority of users.

To resolve the issue, the networking team identified the misconfiguration and restored the correct settings on the load balancer, ensuring that traffic was evenly distributed across all backend servers. Once the configuration was fixed, normal service resumed immediately, and API response times returned to their usual levels.

### Corrective and Preventative Measures:

To prevent similar incidents in the future, the following measures will be implemented:

- **Configuration Review Process**: Implement a mandatory peer-review process for all changes to critical infrastructure configurations, including load balancers.
- **Automated Configuration Validation**: Develop automated scripts to validate load balancer configurations before deployment, ensuring traffic routing settings are correct.
- **Enhanced Monitoring**: Add specific monitoring and alerts for load balancer traffic distribution to detect imbalances more quickly.
- **Incident Response Training**: Provide additional training for engineers on diagnosing load balancer-related issues to reduce investigation time.

### Task List:
- [ ] Implement automated load balancer configuration validation scripts.
- [ ] Add monitoring for load balancer traffic distribution.
- [ ] Develop a peer-review checklist for configuration changes.
- [ ] Conduct a post-incident review meeting to refine incident response protocols. 

This postmortem will be reviewed in our next engineering team meeting to ensure all corrective measures are understood and implemented promptly.
