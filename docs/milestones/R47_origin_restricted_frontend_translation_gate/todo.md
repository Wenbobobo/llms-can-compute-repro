# R47 Todo

- fix one exact restricted frontend bridge onto the existing useful-case
  contract rather than introducing a new runtime stack;
- keep the admissible frontend surface inside bounded `i32`, bounded locals,
  structured loop/branch, and static memory only;
- reuse the landed `R44/R46` useful kernels and exactness harness rather than
  widening the evidence contract;
- stop on the first excluded feature, translation ambiguity, or exact
  free-running execution break; and
- export enough machine-readable artifacts for later explicit `H46`
  interpretation without widening claims here.
