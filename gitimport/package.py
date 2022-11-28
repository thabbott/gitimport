import sys
import os
import tempfile
import subprocess

# Find git command
def _find_git():
    git = shutil.which('git')
    if not git:
        raise EnvironmentError('Could not find git. Is it installed?')
    return git

# Clone the git repository at `path` in the directory `dest`
def _clone(path, dest, branch):
    git = _find_git()
    if branch:
        args = [git, 'clone', '--bare', '--branch', branch, path, dest])
    else:
        args = [git, 'clone', '--bare', path, dest]
    result = subprocess.run(args)
    if result.returncode != 0:
        shutil.rmtree(dest)
        raise ValueError(
            'git clone failed with path ' +
            path if not branch else f'{path} and branch {branch}'
        )

# Check out a specific commit
def _checkout(dest, commit):
    git = _find_git()
    args = [git, 'checkout', commit]
    result = subprocess.run(args)
    if result.returncode != 0:
        shutil.rmtree(dest)
        raise ValueError(f'git checkout failed with commit hash {commit}')

def use(path, branch=None, commit=None, prefix=None, add_to_path=True):
    """
    Create a temporary copy of a package and return the path.
    
    Parameters:
    
    path: str
        Path to the location of a Python package. Can be a directory on
        a local filesystem or the URL of a git repository.
        
    branch: str, optional
        Git branch name. If provided, `create` will check out the specified
        branch, and will raise an exception if the package that `path` points
        to is not a git repository.'
        
    commit: str, optional
        Git commit hash. If provided, `create` will check out the specified
        commit, and will raise an exception if the package that `path` points
        to is not a git repository.
        
    prefix: str, optional
        If provided, create the copy in a directory called `prefix`, but
        only add its parent directory to `sys.path`. This allows code like
        `from prefix import ...` to load modules in the package.
        
    add_to_path: bool, optional
        If True, add the temporary copy to `sys.path`.
    """
    
    # Create directory for holding package
    tdir = tempfile.mkdtemp(prefix=config['package_dir'])
    dest = tdir if not prefix else os.path.join(tdir, prefix)
    os.makedirs(dest, exist_ok=True)
    
    # Clone git repository
    _clone(path, dest, branch)

    # Switch to commit if necessary
    if commit:
        _checkout(dest, commit)
        
    # Append package to path unless prevented
    if add_to_path:
        sys.path.append(tdir)
        
    return dest
    