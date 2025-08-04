// gatling/simulations/BasicSimulation.scala
package simulations

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BasicSimulation extends Simulation {

  val httpProtocol = http.baseUrl("http://host.docker.internal:5000") 

  val scn = scenario("Basic Load Test")
    .exec(
      http("Get Root")
        .get("/")
        .check(status.is(200))
    )
    .pause(1)

  setUp(
    scn.inject(atOnceUsers(10))
  ).protocols(httpProtocol)
}
