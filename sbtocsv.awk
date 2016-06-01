function join(array, start, end, sep, result, i)
{
    if (sep == "")
       sep = " ";
    else if (sep == SUBSEP) # magic value
       sep = "";
    result = array[start];
    for (i = start + 1; i <= end; i++)
        result = result sep array[i];
    return result;
}
/Number of threads:/           { i = 0 ; csv[i++] = $4; }
/transactions:/                { csv[i++] = $2; }
/read.write requests:/         { csv[i++] = $3; }
/min:/                         { sub("ms", "", $2); csv[i++] = $2; }
/max:/                         { sub("ms", "", $2); csv[i++] = $2; }
/approx.  *95 percentile:/     { sub("ms", "", $4); csv[i++] = $4; }
/execution time .avg.stddev.:/ { print join(csv,0,i-1,","); }
