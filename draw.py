from display import *
from matrix import *
from math import *

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(points, x0, y0, z0)
    add_point(points, x1, y1, z1)
    add_point(points, x2, y2, z2)

def frontFacing(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    A = [x1 - x0, y1 - y0, z1 - z0]
    B = [x2 - x0, y2 - y0, z2 - z0]

    normal = [A[1] * B[2] - A[2] * B[1], A[2] * B[0] - A[0] * B[2], A[0] * B[1] - A[1] * B[0]]

    return (normal[2] > 0)

def draw_polygons( points, screen, color ):
    point = 0
    while point < len(points) - 2:
        x0 = int(points[point][0])
        y0 = int(points[point][1])
        z0 = int(points[point][2])
        
        x1 = int(points[point+1][0])
        y1 = int(points[point+1][1])
        z1 = int(points[point+1][2])
        
        x2 = int(points[point+2][0])
        y2 = int(points[point+2][1])
        z2 = int(points[point+2][2])
        
        if (frontFacing(x0, y0, z0, x1, y1, z1, x2, y2, z2)):
            draw_line(x0, y0, x1, y1, screen, color)
            draw_line(x1, y1, x2, y2, screen, color)
            draw_line(x2, y2, x0, y0, screen, color)
        point += 3


def add_box( points, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #counterclockwise...
    add_polygon( points, x, y, z, x, y1, z, x1, y, z );
    add_polygon( points, x, y1, z, x1, y1, z,  x1, y, z );
    
    add_polygon( points, x1, y1, z, x1, y, z1, x1, y, z );
    add_polygon( points, x1, y1, z, x1, y1, z1,  x1, y, z1 );
    
    add_polygon( points, x, y, z, x, y1, z1, x, y1, z );
    add_polygon( points, x, y, z, x, y, z1, x, y1, z1 );
    
    add_polygon( points, x1, y, z, x1, y, z1, x, y, z1 );
    add_polygon( points, x1, y, z, x, y, z1, x, y, z );
    
    add_polygon( points, x1, y1, z, x, y1, z, x, y1, z1 );
    add_polygon( points, x1, y1, z, x, y1, z1, x1, y1, z1 );
    
    add_polygon( points, x1, y, z1, x1, y1, z1,x, y1, z1 );
    add_polygon( points, x1, y, z1, x, y1, z1, x, y, z1 );
    
    #front
    # add_edge(points, x, y, z, x+2, y+2, z+2)
    # add_edge(points, x, y1, z, x+2, y1+2, z+2)
    # add_edge(points, x1, y, z, x1+2, y+2, z+2)
    # add_edge(points, x1, y1, z, x1+2, y1+2, z+2)

    #back
    # add_edge(points, x, y, z1, x+2, y+2, z1+2)
    # add_edge(points, x, y1, z1, x+2, y1+2, z1+2)
    # add_edge(points, x1, y, z1, x1+2, y+2, z1+2)
    # add_edge(points, x1, y1, z1, x1+2, y1+2, z1+2)

def add_sphere( edges, cx, cy, cz, r, step ):
    points = generate_sphere(cx, cy, cz, r, step)
    num_steps = int(1/step+0.1)
    
    lat_start = 0
    lat_stop = num_steps
    longt_start = 0
    longt_stop = num_steps

    num_steps+= 1
    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):
            index = lat * num_steps + longt
            
            # add_polygon( edges,
                         
            #              points[index][0],
            #              points[index][1],
            #              points[index][2],

            #              points[index + 1][0],
            #              points[index + 1][1],
            #              points[index + 1][2],

            #              points[(index + num_steps) % (lat_stop * num_steps)][0],
            #              points[(index + num_steps) % (lat_stop * num_steps)][1],
            #              points[(index + num_steps) % (lat_stop * num_steps)][2] )

            # add_edge(edges, points[index][0],
            #          points[index][1],
            #          points[index][2],
            #          points[index][0]+1,
            #          points[index][1]+1,
            #          points[index][2]+1 )

            x0 = points[index][0]
            y0 = points[index][1]
            z0 = points[index][2]
            
            x1 = points[(index + 1) % len(points)][0]
            y1 = points[(index + 1) % len(points)][1]
            z1 = points[(index + 1) % len(points)][2]

            x2 = points[(index + num_steps) % len(points)][0]
            y2 = points[(index + num_steps) % len(points)][1]
            z2 = points[(index + num_steps) % len(points)][2]

            x3 = points[(index + num_steps + 1) % len(points)][0]
            y3 = points[(index + num_steps + 1) % len(points)][1]
            z3 = points[(index + num_steps + 1) % len(points)][2]

            add_polygon(edges, x1, y1, z1, x2, y2, z2, x0, y0, z0)
            add_polygon(edges, x2, y2, z2, x1, y1, z1, x3, y3, z3)

def generate_sphere( cx, cy, cz, r, step ):
    points = []
    num_steps = int(1/step+0.1)
    
    rot_start = 0
    rot_stop = num_steps
    circ_start = 0
    circ_stop = num_steps
            
    for rotation in range(rot_start, rot_stop):
        rot = step * rotation
        for circle in range(circ_start, circ_stop+1):
            circ = step * circle

            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2*math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2*math.pi * rot) + cz

            points.append([x, y, z])
            #print 'rotation: %d\tcircle%d'%(rotation, circle)
    return points
        
def add_torus( edges, cx, cy, cz, r0, r1, step ):
    points = generate_torus(cx, cy, cz, r0, r1, step)
    num_steps = int(1/step+0.1)
    
    lat_start = 0
    lat_stop = num_steps
    longt_start = 0
    longt_stop = num_steps
    
    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):
            index = lat * num_steps + longt
            
            # add_polygon( edges,
                         
            #                  points[index][0],
            #                  points[index][1],
            #                  points[index][2],
            
            #                  points[(index + 1) % (len(points))][0],
            #                  points[(index + 1) % (len(points))][1],
            #                  points[(index + 1) % (len(points))][2],
        
            #                  points[(index + num_steps) % (len(points))][0],
            #                  points[(index + num_steps) % (len(points))][1],
            #                  points[(index + num_steps) % (len(points))][2] )
            # add_polygon( edges,
            
            #              points[(index + 1) % (len(points))][0],
            #              points[(index + 1) % (len(points))][1],
            #              points[(index + 1) % (len(points))][2],
            
            #              points[(index + num_steps) % (len(points))][0],
            #              points[(index + num_steps) % (len(points))][1],
            #              points[(index + num_steps) % (len(points))][2],
            
            #              points[(index + num_steps + 1) % (len(points))][0],
            #              points[(index + num_steps + 1) % (len(points))][1],
            #              points[(index + num_steps + 1) % (len(points))][2] )

            x0 = points[index][0]
            y0 = points[index][1]
            z0 = points[index][2]
        
            x1 = points[(index + 1) % len(points)][0]
            y1 = points[(index + 1) % len(points)][1]
            z1 = points[(index + 1) % len(points)][2]

            x2 = points[(index + num_steps) % len(points)][0]
            y2 = points[(index + num_steps) % len(points)][1]
            z2 = points[(index + num_steps) % len(points)][2]

            x3 = points[(index + num_steps + 1) % len(points)][0]
            y3 = points[(index + num_steps + 1) % len(points)][1]
            z3 = points[(index + num_steps + 1) % len(points)][2]
        
            add_polygon(edges, x1, y1, z1, x2, y2, z2, x0, y0, z0)
            add_polygon(edges, x2, y2, z2, x1, y1, z1, x3, y3, z3)
        
            # add_edge(edges, points[index][0],
            #          points[index][1],
            #          points[index][2],
            #          points[index][0]+1,
            #          points[index][1]+1,
            #          points[index][2]+1 )

def generate_torus( cx, cy, cz, r0, r1, step ):
    points = []
    num_steps = int(1/step+0.1)
    
    rot_start = 0
    rot_stop = num_steps
    circ_start = 0
    circ_stop = num_steps

    print num_steps
    
    for rotation in range(rot_start, rot_stop):
        rot = step * rotation
        for circle in range(circ_start, circ_stop):
            circ = step * circle

            x = math.cos(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cx;
            y = r0 * math.sin(2*math.pi * circ) + cy;
            z = -1*math.sin(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cz;

            points.append([x, y, z])
    return points

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    t = step

    while t <= 1.00001:
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    t = step
    while t <= 1.00001:
        x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]
                
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
