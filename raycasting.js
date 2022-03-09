function rayCasting(screen, map, player) {
    let precision = 64;
    let incrementAngle = player.fieldOfView / screen.width;
  
    let wallHeights = [];
    let rayAngle = player.angle - player.fieldOfView / 2;
    for(let rayCount = 0; rayCount < screen.width; rayCount++) {
  
      // start the ray at the player position
      let ray = {
        x: player.x,
        y: player.y
      };
  
      // the ray moves at constant increments
      let rayCos = Math.cos(degreeToRadians(rayAngle)) / precision;
      let raySin = Math.sin(degreeToRadians(rayAngle)) / precision;
  
      // advance the ray until it finds a wall (a non zero tile)
      let wall = 0;
      while(wall == 0) {
        ray.x += rayCos;
        ray.y += raySin;
        wall = map[Math.floor(ray.y)][Math.floor(ray.x)];
      }
  
      // calculate the distance from the player to the wall hit
      let distance = Math.sqrt(Math.pow(player.x - ray.x, 2) + Math.pow(player.y - ray.y, 2));
  
      // calculate height at current x inversely proportional to the distance
      wallHeights.push(Math.floor(screen.halfHeight / distance));
  
      // increment the angle for the next ray
      rayAngle += incrementAngle;
    }
  
    return wallHeights;
  }