---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Shadow Ray)[^1]
> A secondary ray, distinct from a viewing ray, cast from a shaded point $\mathbf{p}$ toward a light source to determine whether the light is blocked: if the shadow ray hits an object before reaching the light, $\mathbf{p}$ is in shadow with respect to that light and receives no direct illumination from it.

# Properties
- Used within [[Ray Tracing]] to add shadows to a [[Shading]] model; if multiple lights are present, one shadow ray is cast per light.
- The [[Ray Intersection]] test for a shadow ray excludes a small interval near its origin, avoiding a spurious self-intersection with the surface $\mathbf{p}$ lies on due to numerical imprecision.
- Ambient shading is unaffected by shadow rays, since [[Ambient Shading]] is added regardless of whether the point is in shadow.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=102&annotation=C8DSEJFJ)
