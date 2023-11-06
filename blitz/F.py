

def main():
    s = []
    for _ in range(int(input())):
        cmd, v = list(map(int, input().split()))
        s.append(((lambda x,y: x), ))
        a = True
        if cmd == 1: #max
            while s:
                if s[-1][0] == max and s[-1][1] <= v:
                    s.pop()
                if s[-1][0] == min and s[-1][1] <= v:
                    s.clear()
                    s.append(((lambda x,y: y), v))
                    a = False
                    break
                if s[-1][0] == min and s[-1][1] > v:
                    break
                if s and s[-1][0] == max and s[-1][1] >= v:
                    a = False
                    break
                break
            if a:
                s.append((max, v))
        elif cmd == 2: #min
            while s:
                if s[-1][0] == max and s[-1][1] <= v:
                    break
                if s[-1][0] == min and s[-1][1] <= v:
                    a = False
                    break
                if s[-1][0] == min and s[-1][1] > v:
                    s.pop()
                if s and s[-1][0] == max and s[-1][1] >= v:
                    s.clear()
                    s.append(((lambda x,y: y), v))
                    a = False
                    break
                break
            if a:
                s.append((min, v))

        elif cmd == 3:
            for f, a in s:
                v = f(v,a)
            print(v)

def test_main():
   # Test case 1
   input_values = ['3', '1 10', '2 5', '3']
   expected_output = '10'
   assert main(input_values) == expected_output

   # Test case 2
   input_values = ['4', '2 3', '1 2', '2 1', '3']
   expected_output = '1'
   assert main(input_values) == expected_output

   # Test case 3
   input_values = ['3', '1 10', '1 20', '3']
   expected_output = '20'
   assert main(input_values) == expected_output

   # Test case 4
   input_values = ['3', '2 3', '2 1', '3']
   expected_output = '1'
   assert main(input_values) == expected_output

main()


