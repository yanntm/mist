vars
     x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13
rules
    x0 >= 1 ->
		    x0' = x0-1 ,
		    x1' = x1+1 ;

    x4 >= 1 , x9 >= 1 ->
		    x0' = x0+1 ,
		    x2' = x2+1 ,
		    x4' = x4-1 ,
		    x9' = x9-1 ;

    x4 >= 1 , x6 >= 1 ->
		    x0' = x0+1 ,
		    x3' = x3+1 ,
		    x4' = x4-1 ,
		    x6' = x6-1 ;

    x1 >= 1 , x3 >= 1 ->
		    x1' = x1-1 ,
		    x3' = x3-1 ,
		    x5' = x5+1 ,
		    x6' = x6+1 ;

    x1 >= 1 , x2 >= 1 ->
		    x1' = x1-1 ,
		    x2' = x2-1 ,
		    x5' = x5+1 ,
		    x9' = x9+1 ;

    x5 >= 1 ->
			x4' = x4+1 ,
		       	x5' = x5-1 ;

    x10 >= 1 ->
		    x7' = x7+1 ,
		    x10' = x10-1 ;

    x7 >= 1 ->
		    x7' = x7-1 ,
		    x8' = x8+1 ;

    x6 >= 1 , x8 >= 1 ->
		    x6' = x6-1 ,
		    x8' = x8-1 ,
		    x9' = x9+1 ;

    x9 >= 1 ->
		    x6' = x6+1 ,
		    x9' = x9-1 ,
		    x10' = x10+1 ;

    x10 >= 1 ->
			x10' = x10-1 ,
			x12' = x12+1 ;

    x11 >= 1 ->
		    x8' = x8+1 ,
		    x11' = x11-1 ,
		    x13' = x13+1 ;

    x12 >= 1 , x13 >= 1 ->
		    x11' = x11+1 ,
		    x12' = x12-1 ,
		    x13' = x13-1 ;


init
    x0 = 0 , x1 = 0 , x2 = 0 , x3 = 0 , x4 = 0 , x5 = 1 , x6 = 1 , x7 >= 1 , x8 = 0 , x9 = 0 , x10 = 0 , x11 = 0 , x12 = 0 , x13 = 1

target
    x9 >= 2

invariants
x2 = 1, x3 = 1, x4 = 1, x5 = 1
x0 = 1, x1 = 1, x4 = 1, x5 = 1
x11 = 1, x13 = 1
