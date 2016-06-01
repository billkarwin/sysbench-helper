BEGIN {
  srand(8675309+CSVOFFSET);
  for (id = CSVOFFSET; id <= CSVLENGTH; id+=CSVPARTITIONS) {
    k = int(rand()*1000000);
    c = sprintf("%011d-%011d-%011d-%011d-%011d-%011d-%011d-%011d-%011d-%011d",
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999));
    pad = sprintf("%011d-%011d-%011d-%011d-%011d",
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999),
      int(rand()*99999999999));
    printf("%d,%d,%s,%s\n", id, k, c, pad);
  }
}
