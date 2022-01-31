## Bugs Fixed 

- Fix for [Favicon 401 error](https://medium.com/@aurelien.delogu/401-error-on-a-webmanifest-file-cb9e3678b9f3) found as resolved using the site linked.
- Bug using [Bulma columns](https://github.com/jgthms/bulma/issues/449) creates overflow on mobile as there is margin top, left and right of 0.75rem so addressed this in CSS using margin: 0 !important; on columns.


## Known Bugs
- AllAuth automatically logs user out before displaying Sign Out page

