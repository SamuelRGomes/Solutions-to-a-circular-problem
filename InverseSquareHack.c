float Q_rsqrt( float number )
{
	long i;
	float x2, y;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       
	i  = 0x5f3759df - ( i >> 1 );              
	y  = * ( float * ) &i;
	y  = y * ( 1.5F - ( x2 * y * y ) );  

	return y;
}

// Central useful concepts for the development of the algorithm : https://en.wikipedia.org/wiki/Fast_inverse_square_root#:~:text=in%20IEEE%20754%20floating%2Dpoint,reflection%20for%20lighting%20and%20shading.
// https://betterexplained.com/articles/understanding-quakes-fast-inverse-square-root/