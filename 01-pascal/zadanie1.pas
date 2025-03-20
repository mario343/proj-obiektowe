program zadanie1;

procedure RandomNumbers(fromNum, toNum, size: integer; var arr: array of integer);
var
  i: integer;

begin
  Randomize; 

  Writeln;
  writeln('Before sorting:');  

  for i := 0 to size-1 do
  begin
    arr[i] := Random(toNum - fromNum + 1) + fromNum;
    Write(arr[i], ' ');
  end;

  Writeln;
  Writeln;

end;


procedure BubbleSort(var arr: array of integer);
var
  i, j, temp: integer;
  swapped: boolean;
begin
  if Length(arr) <= 1 then
    Exit; 

  for i := Low(arr) to High(arr) - 1 do
  begin
    swapped := False;
    for j := Low(arr) to High(arr) - i - 1 do
    begin
      if arr[j] > arr[j + 1] then
      begin
        temp := arr[j];
        arr[j] := arr[j + 1];
        arr[j + 1] := temp;
        swapped := True;
      end;
    end;
    if not swapped then
      Break;  
  end;

  writeln('After sorting:');
  for i := Low(arr) to High(arr) do
    write(arr[i], ' ');
  writeln;
end;

var
  fromNum, toNum, size: integer;
    // this is because we are using 1 array and want to give 2 procedures to access it
  arr: array of integer;

begin
    writeln('Enter the min and max value and size of generated numbers (the total numbers in the list): ');
    
    writeln('Enter the min value:');
    readln(fromNum);
    
    writeln('Enter the max value:');
    readln(toNum);
    
    writeln('Enter the size of generated numbers:');
    readln(size);

    // memory allocation
    SetLength(arr, size);

    RandomNumbers(fromNum, toNum, size, arr); 

    BubbleSort(arr);

end. 

