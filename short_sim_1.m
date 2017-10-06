y = 20;
n = 10;
K = 500;
eta = 0.00001;

a = ones(K,1);
for i = 1:K-1
    a(i+1) = a(i) - eta*2*n*a(i)^(n-1)*(a(i)^n - y);
end


b = ones(K,1);
for i = 1:K-1
    b(i+1) = (1 - 2 * eta * n^2 * y^(2-2/n)) * a(i) + 2 * eta * n^2 * y^(2-1/n);
end

% y_line = ones(K,1) * (y^(1/n));
% plot(y_line);
% hold on;
% plot(a);
% hold on;
% plot(b)

residual = abs(a-b);
semilogy(residual)