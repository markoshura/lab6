+input=open('input.txt', 'r')
+output=open('output.txt', 'w')
+N = int(input.readline())
+lis = list(map(int, input.readline().split()))
+nf = 0
+hf = 0
+for i in range(N):
+    if lis[i] == 5:
+        hf+= 1
+    else:
+        hf -= (lis[i]-5)//5
+        if hf < 0:
+            nf -= hf
+            hf = 0
+print(nf, file=output)
